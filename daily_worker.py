import datetime
import json

import lxml.html

from infrastructure import redis, log, rabbitmq
from utils import request

MAX_DAILY_PAGER = 5000


def make_daily_url(pager):
    return "https://www.bilibili.com/newlist.html?page=%s" % pager


def daily_job():
    log.info(log.TARGET_DAILY_PAGER, "Start fetch last day uploaded videos")

    # 小于一个固定的翻页页数
    while redis.Context.daily_pager_index < MAX_DAILY_PAGER:

        log.info(log.TARGET_DAILY_PAGER, "Fetching new list", {"url": make_daily_url(redis.Context.daily_pager_index)})

        daily_html = request.get(make_daily_url(redis.Context.daily_pager_index))

        if not daily_html:
            log.warning(log.TARGET_DAILY_PAGER, "daily page has no html response",
                        {"url": make_daily_url(redis.Context.daily_pager_index)})
            continue

        daily_dom = lxml.html.etree.HTML(daily_html)
        video_items = daily_dom.xpath("//*[contains(@class,'vd_list')]/li")

        print("cur page: %s" % make_daily_url(redis.Context.daily_pager_index))
        redis.Context.daily_pager_index += 1

        for vi in video_items:
            date_str = vi.xpath("div[@class='w_info']/i[@class='date']/text()")
            now = datetime.datetime.now()
            now = datetime.datetime(now.year, now.month, now.day)

            date_str = date_str or ["01/01 00:00"]
            date_pub_str = date_str[0].split(" ")[0].split("/")
            date_pub = datetime.datetime(now.year, int(date_pub_str[0]), int(date_pub_str[1]))

            video_url = "https://www.bilibili.com%s" % vi.xpath("a[@class='title']/@href")[0]
            rabbitmq.send(json.dumps({"type": "video", "url": video_url}), rabbitmq.PRIORITY_VIDEO_FROM_DAILY)

            log.info(log.TARGET_DAILY_PAGER, "New video will in queue", {"url": video_url, "date": date_pub,
                                                                         "title": (vi.xpath(
                                                                             "a[@class='title']/text()") or [""])[0]})

    log.info(log.TARGET_DAILY_PAGER, "Fetching new list finished")


if __name__ == "__main__":
    daily_job()
