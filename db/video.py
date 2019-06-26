from typing import List
from db import _cur, _conn


def create_videos_item(vid: int, title: str, ptype: str, ctype: str, describe: str,
                       upload_time: str, author_name: str, author_id: int, tags: List[str],
                       duration: int, cover_url: str):
    _cur.execute(
        """
        insert into videos 
        (vid, title, ptype, ctype, describe, upload_time, author_name, author_id, tags, duration, cover_url)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (vid, title, ptype, ctype, describe, upload_time, author_name, author_id, tags, duration, cover_url)
    )
    _conn.commit()


def create_videos_increment_item(vid: int, danmu_count: int, play_count: int, reply_count: int,
                                 like_count: int, coin_count: int, collect_count: int, charger_count: int):
    _cur.execute(
        """
        insert into videos_increment 
        (vid, danmu_count, play_count, reply_count, like_count, coin_count, collect_count, charger_count)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (vid, danmu_count, play_count, reply_count, like_count, coin_count, collect_count, charger_count)
    )
    _conn.commit()


def create_videos_related_item(vid: int, related_vid: int):
    _cur.execute(
        """
        insert into videos_related
        (vid, related_vid)
        values (%s, %s, %s)
        """,
        (vid, related_vid)
    )
    _conn.commit()
