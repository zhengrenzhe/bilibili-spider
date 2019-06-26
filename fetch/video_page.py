import json
import re
from datetime import datetime

from utils.request import get
import lxml.html


def _extract_base_info(video_data):
    return {
        "vid": video_data["data"]["aid"],
        "title": video_data["data"]["title"],
        # ptype 需要从html中提取
        "ptype": None,
        "ctype": video_data["data"]["tname"],
        "desc": video_data["data"]["desc"],
        "upload_time": datetime.fromtimestamp(video_data["data"]["pubdate"]),
        # spider_get_time 需判断是不是第一次提取
        "spider_get_time": None,
        "author_name": video_data["data"]["owner"]["name"],
        "author_id": video_data["data"]["owner"]["mid"],
        "tags": [],
        "duration": video_data["data"]["duration"],
        "cover_url": video_data["data"]["pic"]
    }


def _extract_increment_info(video_data):
    return {
        "spider_update_time": datetime.now(),
        "danmu_count": video_data["data"]["stat"]["danmaku"],
        "play_count": video_data["data"]["stat"]["view"],
        "reply_count": video_data["data"]["stat"]["reply"],
        "like_count": video_data["data"]["stat"]["like"],
        "coin_count": video_data["data"]["stat"]["coin"],
        "collect_count": video_data["data"]["stat"]["favorite"],
        "share_count": video_data["data"]["stat"]["share"],
    }


def fetch_video_page(url: str):
    vid = re.search(r"video/av(\d+)", url)

    if vid and len(vid.groups()) != 1:
        return

    vid = vid.groups()[0]

    video_data = get("https://api.bilibili.com/x/web-interface/view?aid=%s" % vid)
    video_data = json.loads(video_data)

    video_base_info = _extract_base_info(video_data)
    video_increment_info = _extract_increment_info(video_data)

    video_html = get(url)
    video_dom = lxml.html.etree.HTML(video_html)

    types = video_dom.xpath("//*[contains(@class,'a-crumbs')]/a/text()")
    if len(types) == 2:
        video_base_info["ptype"] = types[0]

    related_videos = video_dom.xpath("//*[contains(@class,'video-page-card')]//div[@class='info']/a/@href")
    video_related_info = [int(re.search(r"video/av(\d+)", v).groups()[0]) for v in related_videos]

    return {
        "video_base_info": video_base_info,
        "video_increment_info": video_increment_info,
        "video_related_info": video_related_info,
    }
