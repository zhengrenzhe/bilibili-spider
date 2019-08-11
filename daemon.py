import json
from multiprocessing import Process

from apscheduler.schedulers.blocking import BlockingScheduler

import fetch_daily
import video_listener
from mq import create_connect


def daily_videos():
    scheduler = BlockingScheduler()
    scheduler.add_job(fetch_daily.work, 'cron', hour=1)
    scheduler.start()


daily_process = Process(target=daily_videos)
daily_process.start()


def url_job(ch, method, properties, body):
    b = json.loads(body)
    if b["type"] == "video":
        print(b["url"])
        video_listener.work(b["url"])


cha = create_connect()
cha.basic_consume(queue='video_urls', auto_ack=True, on_message_callback=url_job)
cha.start_consuming()
