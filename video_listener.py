from fetch import fetch_video_page
from db.video import create_videos_item, create_videos_increment_item, create_videos_related_item


def work(url: str):
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


work("https://www.bilibili.com/video/av56617044/?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.21")
