from datetime import datetime
from typing import List

from infrastructure import log, postgres

conn = postgres.CONN
cur = postgres.CUR


def get_videos_count():
    cur.execute(
        """
        SELECT reltuples AS approximate_row_count FROM pg_class WHERE relname = 'videos';
        """
    )
    results = cur.fetchone()
    return results[0]


def create_videos_item(vid: int, title: str, ptype: str, ctype: str, describe: str,
                       upload_time: datetime, author_name: str, author_id: int, tags: List[str],
                       duration: int, cover_url: str):
    try:
        cur.execute(
            """
            insert into videos 
            (vid, title, ptype, ctype, describe, upload_time, author_name, author_id, tags, duration, cover_url)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (vid, title, ptype, ctype, describe, upload_time, author_name, author_id, tags, duration, cover_url)
        )
    except Exception as e:
        log.error(log.TARGET_DATABASE, str(e), {"vid": vid})
        conn.rollback()
    else:
        log.info(log.TARGET_DATABASE, "Write db:videos_item success", {"vid": vid})
        conn.commit()


def create_videos_increment_item(vid: int, danmu_count: int, play_count: int, reply_count: int,
                                 like_count: int, coin_count: int, collect_count: int, share_count: int):
    try:
        cur.execute(
            """
            insert into videos_increment 
            (vid, danmu_count, play_count, reply_count, like_count, coin_count, collect_count, share_count)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (vid, danmu_count, play_count, reply_count, like_count, coin_count, collect_count, share_count)
        )
    except Exception as e:
        log.error(log.TARGET_DATABASE, str(e), {"vid": vid})
        conn.rollback()
    else:
        log.info(log.TARGET_DATABASE, "Write db:videos_increment_item success", {"vid": vid})
        conn.commit()


def create_videos_related_item(vid: int, related_vid: List[int]):
    try:
        cur.execute(
            """
            insert into videos_related
            (vid, related_vid)
            values (%s, %s)
            """,
            (vid, related_vid)
        )
    except Exception as e:
        log.error(log.TARGET_DATABASE, str(e), {"vid": vid})
        conn.rollback()
    else:
        log.info(log.TARGET_DATABASE, "Write db:videos_related_item success", {"vid": vid})
        conn.commit()


def get_all_vids():
    cur.execute(
        """
        SELECT vid from videos;
        """
    )
    results = cur.fetchall()
    return results
