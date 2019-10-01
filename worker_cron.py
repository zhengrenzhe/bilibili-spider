"""
cron jobs
"""

import time

import schedule

from infrastructure import redis, log
from worker_daily import daily_job


def fetch_last_7_days_videos():
    log.info(log.TARGET_CRON, "fetch last 7 days videos job start")
    print("fetchLastDayVideos")


def daily_fetch_pagers():
    log.info(log.TARGET_CRON, "daily fetch job start")
    redis.Context.daily_pager_index = 0
    redis.Context.clear_all_visited()
    daily_job()


schedule.every().days.at("03:00").do(fetch_last_7_days_videos)
schedule.every().days.at("00:01").do(daily_fetch_pagers)

while True:
    log.info(log.TARGET_CRON, "Cron Jobs check")
    schedule.run_pending()
    time.sleep(60)
