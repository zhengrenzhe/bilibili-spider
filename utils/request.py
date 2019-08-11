import gzip
import time
from os import path
from random import choice
from urllib import request, parse, error

from pycookiecheat import chrome_cookies
from yaml import load, Loader

import log

UA = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0"
]

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6,et;q=0.5",
    "Cache-Control": "no-cache",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": choice(UA)
}

proxy_config = load(open(path.join(path.dirname(path.abspath(__file__)), "../proxy.yaml")), Loader=Loader)
proxy_url = "http://%(username)s:%(password)s@%(host)s:%(port)s" % proxy_config

log.info("Use proxy: %s" % proxy_url)

proxy_handler = request.ProxyHandler({
    "http": proxy_url,
    "https": proxy_url,
})

proxy_opener = request.build_opener(proxy_handler)
# request.install_opener(proxy_opener)

cookies = chrome_cookies("https://www.bilibili.com")
HEADERS["Cookie"] = ";".join(["%s=%s" % (k, cookies[k]) for k in cookies])


def _get(url: str, retry_num: int):
    log.info("Start HTTP request", {"url": url})
    if retry_num != 0:
        log.info("Retry http get request", {"url": url, "retry_num": retry_num})

    HEADERS["Host"] = parse.urlparse(url).netloc
    req = request.Request(url, headers=HEADERS)
    res = request.urlopen(req)
    res_text = res.read()

    print(res_text)

    log.info("Finished HTTP request", {"url": url, "status_code": res.status})
    try:
        return gzip.decompress(res_text).decode("utf-8")
    except:
        return res_text.decode("utf-8")


def get(url: str, timeout=0):
    i = 0
    while i < 5:
        try:
            res_text = _get(url, i)
            time.sleep(timeout)
            return res_text
        except (error.URLError, error.HTTPError) as err:
            print(err)
            log.error("HTTP get request error", {"url": url, "error": err})
        i += 1
