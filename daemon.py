from apscheduler.schedulers.background import BackgroundScheduler

import fetch_daily

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_daily.work, 'cron', hour=1)
scheduler.start()
