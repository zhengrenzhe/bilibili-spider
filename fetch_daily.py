import lxml.html
import datetime

import log
from utils import request


def work():
    daily_url = "https://www.bilibili.com/newlist.html?page=1440"
    next_page = True

    while next_page:
        log.info("Fetching newlist", {"url": daily_url})

        daily_html = request.get(daily_url)
        daily_dom = lxml.html.etree.HTML(daily_html)
        video_items = daily_dom.xpath("//*[contains(@class,'vd_list')]/li")

        daily_url = "https://www.bilibili.com%s" % daily_dom.xpath("//*[contains(@class,'nextPage')]/@href")[0]

        before_count = 0

        for vi in video_items:
            date_str = vi.xpath("div[@class='w_info']/i[@class='date']/text()")
            now = datetime.datetime.now()
            now = datetime.datetime(now.year, now.month, now.day)

            if len(date_str) == 1:
                date_pub_str = date_str[0].split(" ")[0].split("/")
                date_pub = datetime.datetime(now.year, int(date_pub_str[0]), int(date_pub_str[1]))
                date_diff = (now - date_pub).days

                # 今天
                if date_diff == 0:
                    pass

                # 昨天
                elif date_diff == 1:
                    video_url = "https://www.bilibili.com%s" % vi.xpath("a[@class='title']/@href")[0]
                    log.info("New video will in queue",
                             {"url": video_url, "date": date_pub,
                              "title": (vi.xpath("a[@class='title']/text()") or [""])[0]})

                # 昨天之前
                else:
                    # 每页中有可能会混入昨天之前的视频，在每一页视频中昨天之前的占比70%以上才停止抓新视频
                    before_count += 1
                    print((before_count / len(video_items)))
                    if (before_count / len(video_items)) > 0.7:
                        log.info("Fetching newlist stopped", {"url": daily_url})
                        next_page = False
                        break
