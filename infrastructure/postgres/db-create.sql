create database bilibili owner postgres;

create table videos
(
    id              serial,
    vid             int unique primary key,
    title           text,
    ptype           text,
    ctype           text,
    describe        text,
    upload_time     timestamp,
    spider_get_time timestamp default current_timestamp,
    author_name     text,
    author_id       int,
    tags            text[],
    duration        int,
    cover_url       text
);

create table videos_increment
(
    id                 serial,
    vid                int,
    spider_update_time timestamp default current_timestamp,
    danmu_count        int,
    play_count         int,
    reply_count        int,
    like_count         int,
    coin_count         int,
    collect_count      int,
    share_count        int
);

create table videos_related
(
    id          serial,
    vid         int,
    related_vid int[]
);


create table author
(
    id          serial,
    author_id   int unique primary key,
    author_name text,
    intro       text,
    avatar      text,
    sex         text,
    level       text,
    birthday    text
);

create table author_increment
(
    id                 serial,
    author_id          int,
    follower_count     int,
    fans_count         int,
    play_count         int,
    charger_count      int,
    videos_count       int,
    spider_update_time timestamp default current_timestamp
);

create table author_videos
(
    id        serial,
    author_id int,
    video_id  int
);