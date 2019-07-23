import lxml.html

from utils import request

daily_url = "https://www.bilibili.com/newlist.html"
daily_html = request.get(daily_url)
daily_dom = lxml.html.etree.HTML(daily_html)

video_urls = daily_dom.xpath("//*[contains(@class,'vd_list')]/li/a[contains(@class,'title')]/@href")

for url_postfix in video_urls:
    url = "https://www.bilibili.com%s" % url_postfix
    print(url)
