from datetime import datetime
from typing import List


class Video:
    def __init__(
            self,
            vid: int,
            title: str,
            ptype: str,
            ctype: str,
            describe: str,
            upload_time: datetime,
            author_name: str,
            author_id: int,
            tags: List[str],
            duration: int,
            cover_url: str
    ):
        self.vid = vid
        self.title = title
        self.ptype = ptype
        self.ctype = ctype
        self.describe = describe
        self.upload_time = upload_time
        self.author_name = author_name
        self.author_id = author_id
        self.tags = tags
        self.duration = duration
        self.cover_url = cover_url


class VideoIncrement:
    def __init__(
            self,
            vid: int,
            danmu_count: int,
            play_count: int,
            reply_count: int,
            like_count: int,
            coin_count: int,
            collect_count: int,
            share_count: int
    ):
        self.vid = vid
        self.danmu_count = danmu_count
        self.play_count = play_count
        self.reply_count = reply_count
        self.like_count = like_count
        self.coin_count = coin_count
        self.collect_count = collect_count
        self.share_count = share_count


class VideoRelated:
    def __init__(
            self,
            vid: int,
            related_vid: List[int]
    ):
        self.vid = vid
        self.related_vid = related_vid
