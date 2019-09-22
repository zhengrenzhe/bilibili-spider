import json
import re
from datetime import datetime
from typing import Tuple

from infrastructure import log
from model.video import Video, VideoIncrement, VideoRelated
from utils.extract import xpath, get_object
from utils.request import get


def _extract(video_html: str):
    if not video_html:
        video_html = "<html></html>"

    video_dom = xpath(video_html)
    video_state = {}
    has_data = False

    for s in video_dom("/html/head/script/text()"):
        if "__INITIAL_STATE__" in s:
            video_state = get_object(s, "__INITIAL_STATE__")
            has_data = True

    vid = int(video_state.get("videoData", {}).get("aid", 0))
    title = video_state.get("videoData", {}).get("title", "")
    ptype = video_dom("//*[@id='viewbox_report']/div[@class='video-data']/span/a[1]/text()")
    ctype = video_state.get("videoData", {}).get("tname", "")
    describe = video_state.get("videoData", {}).get("desc", "")
    upload_time = datetime.fromtimestamp(video_state.get("videoData", {}).get("pubdate", 0))
    author_name = video_state.get("videoData", {}).get("owner", {}).get("name", "")
    author_id = int(video_state.get("videoData", {}).get("owner", {}).get("mid", 0))
    tags = [k.get("tag_name", "") for k in video_state.get("tags", [])]
    duration = int(video_state.get("videoData", {}).get("duration", 0))
    cover_url = video_state.get("videoData", {}).get("pic", "")

    related_videos = video_dom("//*[contains(@class,'video-page-card')]//div[@class='info']/a/@href", always_list=True)

    v = Video(vid=vid, title=title, ptype=ptype, ctype=ctype, describe=describe, upload_time=upload_time,
              author_name=author_name, author_id=author_id, tags=tags, duration=duration, cover_url=cover_url)

    vr = VideoRelated(vid=vid, related_vid=[int(re.search(r"video/av(\d+)", r).groups()[0]) for r in related_videos])

    return has_data, v, vr


def _extract_increment_info(vid: int, video_data):
    has_data = False
    try:
        video_data = json.loads(video_data)
        has_data = True
    except (json.JSONDecodeError, TypeError):
        video_data = {}

    v = VideoIncrement(
        vid=vid,
        danmu_count=int(video_data.get("data", {}).get("stat", {}).get("danmaku", 0)),
        play_count=int(video_data.get("data", {}).get("stat", {}).get("view", 0)),
        reply_count=int(video_data.get("data", {}).get("stat", {}).get("reply", 0)),
        like_count=int(video_data.get("data", {}).get("stat", {}).get("like", 0)),
        coin_count=int(video_data.get("data", {}).get("stat", {}).get("coin", 0)),
        collect_count=int(video_data.get("data", {}).get("stat", {}).get("favorite", 0)),
        share_count=int(video_data.get("data", {}).get("stat", {}).get("share", 0))
    )

    return has_data, v


def parse_video_page(url: str) -> Tuple[bool, Video, VideoIncrement, VideoRelated]:
    log.info(log.TARGET_VIDEO_PAGE, "Start parse video page data", {"url": url})

    vid = int(re.search(r"video/av(\d+)", url).groups()[0])

    # video base data
    video_html = get(url)
    suc1, video_base_data, video_related_data = _extract(video_html)

    # video increment data
    video_quota = get("https://api.bilibili.com/x/web-interface/view?aid=%s" % vid)
    suc2, video_increment_data = _extract_increment_info(vid, video_quota)

    if not suc1:
        print("not html res data")
        log.error(log.TARGET_VIDEO_PAGE, "Video page html request has None response", {"url": url})

    if not suc2:
        print("not api res data")
        log.error(log.TARGET_VIDEO_PAGE, "Video page api request has None response", {"url": url})

    log.info(log.TARGET_VIDEO_PAGE, "Finished parse video page data", {"url": url})

    return suc1 and suc2, video_base_data, video_increment_data, video_related_data
