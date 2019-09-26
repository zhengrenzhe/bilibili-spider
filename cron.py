"""
cron jobs
"""

import time

import schedule

from daily_worker import daily_job
from infrastructure import redis, log


def fetch_last_7_days_videos():
    log.info(log.TARGET_CRON, "fetch last 7 days videos job start")
    print("fetchLastDayVideos")


def daily_fetch_pagers():
    log.info(log.TARGET_CRON, "daily fetch job start")
    redis.Context.daily_pager_index = 0
    daily_job()


schedule.every().days.at("01:00").do(fetch_last_7_days_videos)
schedule.every().days.at("03:00").do(daily_fetch_pagers)

while True:
    schedule.run_pending()
    time.sleep(1)
