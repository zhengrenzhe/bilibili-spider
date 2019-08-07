import lxml.html
import datetime
import json

import log
from mq import MQ
from utils import request

MAX_DAILY_PAGER = 5000


def make_daily_url(pager):
    return "https://www.bilibili.com/newlist.html?page=%s" % pager


def work():
    daily_url_pager = 0
    log.info("Start fetch lastday uploaded videos")

    while daily_url_pager < MAX_DAILY_PAGER:
        log.info("Fetching newlist", {"url": make_daily_url(daily_url_pager)})

        daily_html = request.get(make_daily_url(daily_url_pager))
        daily_dom = lxml.html.etree.HTML(daily_html)
        video_items = daily_dom.xpath("//*[contains(@class,'vd_list')]/li")

        print("cur page: %s" % make_daily_url(daily_url_pager))
        daily_url_pager += 1

        for vi in video_items:
            date_str = vi.xpath("div[@class='w_info']/i[@class='date']/text()")
            now = datetime.datetime.now()
            now = datetime.datetime(now.year, now.month, now.day)

            if len(date_str) == 1:
                date_pub_str = date_str[0].split(" ")[0].split("/")
                date_pub = datetime.datetime(now.year, int(date_pub_str[0]), int(date_pub_str[1]))
                date_diff = (now - date_pub).days

                # 昨天
                if date_diff == 1:
                    video_url = "https://www.bilibili.com%s" % vi.xpath("a[@class='title']/@href")[0]
                    MQ.send(json.dumps({"type": "video", "url": video_url}))
                    log.info("New video will in queue",
                             {"url": video_url, "date": date_pub,
                              "title": (vi.xpath("a[@class='title']/text()") or [""])[0]})

    log.info("Fetching newlist stopped")


if __name__ == "__main__":
    work()
