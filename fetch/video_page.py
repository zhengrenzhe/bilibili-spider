import json
import re
from datetime import datetime
from typing import Tuple

import lxml.html

from utils.request import get
from model.video import Video, VideoIncrement, VideoRelated
import log


def _extract_base_info(video_data):
    return Video(
        vid=int(video_data["data"]["aid"]),
        title=video_data["data"]["title"],
        ptype="",  # 需要从html中提取
        ctype=video_data["data"]["tname"],
        describe=video_data["data"]["desc"],
        upload_time=datetime.fromtimestamp(video_data["data"]["pubdate"]),
        author_name=video_data["data"]["owner"]["name"],
        author_id=video_data["data"]["owner"]["mid"],
        tags=[],
        duration=int(video_data["data"]["duration"]),
        cover_url=video_data["data"]["pic"]
    )


def _extract_increment_info(vid: int, video_data):
    return VideoIncrement(
        vid=vid,
        danmu_count=int(video_data["data"]["stat"]["danmaku"]),
        play_count=int(video_data["data"]["stat"]["view"]),
        reply_count=int(video_data["data"]["stat"]["reply"]),
        like_count=int(video_data["data"]["stat"]["like"]),
        coin_count=int(video_data["data"]["stat"]["coin"]),
        collect_count=int(video_data["data"]["stat"]["favorite"]),
        share_count=int(video_data["data"]["stat"]["share"])
    )


def fetch_video_page(url: str) -> Tuple[Video, VideoIncrement, VideoRelated]:
    log.info("Start parse video page data", {"url": url})

    vid = re.search(r"video/av(\d+)", url).groups()[0]

    video_data = get("https://api.bilibili.com/x/web-interface/view?aid=%s" % vid)
    video_data = json.loads(video_data)

    video_base_info = _extract_base_info(video_data)
    video_increment_info = _extract_increment_info(int(vid), video_data)

    video_html = get(url)
    video_dom = lxml.html.etree.HTML(video_html)

    types = video_dom.xpath("//*[contains(@class,'a-crumbs')]/a/text()")
    if len(types) == 2:
        video_base_info.ptype = types[0]

    tags = video_dom.xpath("//*[contains(@class,'tag-area')]//li[@class='tag']/a/text()")
    if len(tags) != 0:
        video_base_info.tags = tags

    related_videos = video_dom.xpath("//*[contains(@class,'video-page-card')]//div[@class='info']/a/@href")
    video_related_info = VideoRelated(vid=int(vid),
                                      related_vid=[int(re.search(r"video/av(\d+)", v).groups()[0]) for v in
                                                   related_videos])

    log.info("Finished parse video page data", {"url": url})

    return video_base_info, video_increment_info, video_related_info
