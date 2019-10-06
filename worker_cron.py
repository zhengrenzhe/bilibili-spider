"""
cron jobs
"""

import time

import schedule

from infrastructure import log, redis


def fetch_last_7_days_videos():
    pass


def daily_fetch_pagers():
    log.info(log.TARGET_DAILY_PAGER, "reset daily pager index")
    redis.Context.daily_pager_index = 0


schedule.every().days.at("03:00").do(fetch_last_7_days_videos)
schedule.every().days.at("01:00").do(daily_fetch_pagers)

while True:
    log.info(log.TARGET_CRON, "Cron Jobs check")
    schedule.run_pending()
    time.sleep(30)
