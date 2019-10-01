import json
from datetime import datetime

from api import get_video_data
from infrastructure import log, rabbitmq, postgres, redis
from utils.extract import get_vid_from_url


def process_video(url: str):
    vid = get_vid_from_url(url)

    if redis.Context.is_visited(vid):
        return False

    redis.Context.visit(vid)

    ok, res = get_video_data(vid)

    if not ok:
        log.error(log.TARGET_VIDEO_PAGE, "Failre to fetch video page data, will re put in queue", {"url": url})
        rabbitmq.send(json.dumps({"type": "video", "url": url}), rabbitmq.PRIORITY_VIDEO_FROM_DAILY)
        return ok

    base_data = res.get("View", {})
    tag_data = res.get("Tags", [])
    related_data = res.get("Related", [])

    # video meta data
    title = base_data.get("title", "")
    p_type = ""
    c_type = base_data.get("tname", "")
    desc = base_data.get("desc", "")
    upload_time = datetime.fromtimestamp(base_data.get("pubdate", 0))
    author_name = base_data.get("owner", {}).get("name", "")
    author_id = base_data.get("owner", {}).get("mid", "")
    tags = [t.get("tag_name") for t in tag_data]
    duration = base_data.get("duration")
    cover_url = base_data.get("pic")

    # related videos
    related_videos = [r.get("aid", "") for r in related_data]

    # increment data
    danmu_count = base_data.get("stat", {}).get("danmaku", 0)
    play_count = base_data.get("stat", {}).get("view", 0)
    reply_count = base_data.get("stat", {}).get("reply", 0)
    like_count = base_data.get("stat", {}).get("like", 0)
    coin_count = base_data.get("stat", {}).get("coin", 0)
    collect_count = base_data.get("stat", {}).get("favorite", 0)
    share_count = base_data.get("stat", {}).get("share", 0)

    # save video data
    postgres.video.create_videos_item(
        vid=int(vid),
        title=title,
        ptype=p_type,
        ctype=c_type,
        describe=desc,
        upload_time=upload_time,
        author_name=author_name,
        author_id=author_id,
        tags=tags,
        duration=duration,
        cover_url=cover_url
    )

    postgres.video.create_videos_related_item(
        vid=int(vid),
        related_vid=related_videos
    )

    postgres.video.create_videos_increment_item(
        vid=int(vid),
        danmu_count=danmu_count,
        play_count=play_count,
        reply_count=reply_count,
        like_count=like_count,
        coin_count=coin_count,
        collect_count=collect_count,
        share_count=share_count
    )

    # fetch related videos
    for r in related_videos:
        if not redis.Context.is_visited(str(r)):
            r_url = "https://www.bilibili.com/video/av%s" % r
            rabbitmq.send(json.dumps({"type": "video", "url": r_url}), rabbitmq.PRIORITY_VIDEO_FROM_RELATIVE)

    log.info(log.TARGET_VIDEO_PAGE, "Add related videos to queue", {"url": url})
    log.info(log.TARGET_VIDEO_PAGE, "Finished new video page url job", {"url": url})

    return ok
