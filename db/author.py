from db import _cur, _conn


def create_author_item(author_id: int, author_name: str, intro: str, avatar: str, sex: str, level: str, birthday: str):
    _cur.execute(
        """
        insert into author
        (author_id, author_name, intro, avatar, sex, level, birthday)
        values (%s, %s, %s, %s, %s, %s, %s)
        """,
        (author_id, author_name, intro, avatar, sex, level, birthday)
    )
    _conn.commit()


def create_author_increment_item(author_id: int, follower_count: int, fans_count: int, play_count: int,
                                 charger_count: int, videos_count: int):
    _cur.execute(
        """
        insert into author_increment
        (author_id, follower_count, fans_count, play_count, charger_count, videos_count)
        values (%s, %s, %s, %s, %s, %s)
        """,
        (author_id, follower_count, fans_count, play_count, charger_count, videos_count)
    )
    _conn.commit()


def create_author_videos_item(author_id: int, video_id: int):
    _cur.execute(
        """
        insert into author_videos
        (author_id, video_id)
        values (%s, %s)
        """,
        (author_id, video_id)
    )
    _conn.commit()
