from typing import List
import psycopg2

conn = psycopg2.connect(dbname="bilibili", user="postgres", password="1234", host="127.0.0.1")
cur = conn.cursor()


def create_videos_item(vid: int, title: str, ptype: str, ctype: str, describe: str,
                       upload_time: str, author_name: str, author_id: int, tags: List[str],
                       duration: int, cover_url: str):
    cur.execute(
        """
        insert into videos 
        (vid, title, ptype, ctype, describe, upload_time, author_name, author_id, tags, duration, cover_url)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (vid, title, ptype, ctype, describe, upload_time, author_name, author_id, tags, duration, cover_url)
    )
    conn.commit()


def create_videos_increment_item(vid: int, danmu_count: int, play_count: int, reply_count: int,
                                 like_count: int, coin_count: int, collect_count: int, charger_count: int):
    cur.execute(
        """
        insert into videos_increment 
        (vid, danmu_count, play_count, reply_count, like_count, coin_count, collect_count, charger_count)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (vid, danmu_count, play_count, reply_count, like_count, coin_count, collect_count, charger_count)
    )
    conn.commit()


def create_videos_related_item(vid: int, related_vid: int):
    cur.execute(
        """
        insert into videos_related
        (vid, related_vid)
        values (%s, %s, %s)
        """,
        (vid, related_vid)
    )
    conn.commit()


def create_author_item(author_id: int, author_name: str, intro: str, avatar: str, sex: str, level: str, birthday: str):
    cur.execute(
        """
        insert into author
        (author_id, author_name, intro, avatar, sex, level, birthday)
        values (%s, %s, %s, %s, %s, %s, %s)
        """,
        (author_id, author_name, intro, avatar, sex, level, birthday)
    )
    conn.commit()


def create_author_increment_item(author_id: int, follower_count: int, fans_count: int, play_count: int,
                                 charger_count: int, videos_count: int):
    cur.execute(
        """
        insert into author_increment
        (author_id, follower_count, fans_count, play_count, charger_count, videos_count)
        values (%s, %s, %s, %s, %s, %s)
        """,
        (author_id, follower_count, fans_count, play_count, charger_count, videos_count)
    )
    conn.commit()


def create_author_videos_item(author_id: int, video_id: int):
    cur.execute(
        """
        insert into author_videos
        (author_id, video_id)
        values (%s, %s)
        """,
        (author_id, video_id)
    )
    conn.commit()
