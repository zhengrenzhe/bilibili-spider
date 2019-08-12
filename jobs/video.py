import json

from infrastructure import log, rabbitmq, postgres
from parse import parse_video_page


def do(url: str):
    log.info(log.TARGET_VIDEO_PAGE, "Start new video page url job", {"url": url})

    video_base, video_increment, video_related = parse_video_page(url)

    if not video_base:
        return

    postgres.video.create_videos_item(vid=video_base.vid, title=video_base.title, ptype=video_base.ptype,
                                      ctype=video_base.ctype,
                                      describe=video_base.describe, upload_time=video_base.upload_time,
                                      author_name=video_base.author_name, author_id=video_base.author_id,
                                      tags=video_base.tags,
                                      duration=video_base.duration, cover_url=video_base.cover_url)

    postgres.video.create_videos_increment_item(vid=video_increment.vid, danmu_count=video_increment.danmu_count,
                                                play_count=video_increment.play_count,
                                                reply_count=video_increment.reply_count,
                                                like_count=video_increment.like_count,
                                                coin_count=video_increment.coin_count,
                                                collect_count=video_increment.collect_count,
                                                share_count=video_increment.share_count)

    postgres.video.create_videos_related_item(vid=video_related.vid, related_vid=video_related.related_vid)

    for r_vid in video_related.related_vid:
        r_url = "https://www.bilibili.com/video/av%s" % r_vid
        rabbitmq.send(json.dumps({"type": "video", "url": r_url}))
        log.info(log.TARGET_VIDEO_PAGE, "Add related video", {"url": r_url})


if __name__ == "__main__":
    do("https://www.bilibili.com/video/av48401550?spm_id_from=333.334.b_62696c695f646f756761.5")
