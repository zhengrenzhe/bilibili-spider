from fetch import fetch_video_page
from db.video import create_videos_item, create_videos_increment_item, create_videos_related_item
import log


def work(url: str):
    log.info("Start new video page url job", {"url": url})

    video_base, video_increment, video_related = fetch_video_page(url)

    create_videos_item(vid=video_base.vid, title=video_base.title, ptype=video_base.ptype, ctype=video_base.ctype,
                       describe=video_base.describe, upload_time=video_base.upload_time,
                       author_name=video_base.author_name, author_id=video_base.author_id, tags=video_base.tags,
                       duration=video_base.duration, cover_url=video_base.cover_url)

    create_videos_increment_item(vid=video_increment.vid, danmu_count=video_increment.danmu_count,
                                 play_count=video_increment.play_count, reply_count=video_increment.reply_count,
                                 like_count=video_increment.like_count, coin_count=video_increment.coin_count,
                                 collect_count=video_increment.collect_count, share_count=video_increment.share_count)

    create_videos_related_item(vid=video_related.vid, related_vid=video_related.related_vid)

    for r_vid in video_related.related_vid:
        r_url = "https://www.bilibili.com/video/av%s" % r_vid
        log.info("Add related video", {"url": r_url})


work("https://www.bilibili.com/video/av55731626?spm_id_from=333.334.b_62696c695f746563686e6f6c6f6779.4")
