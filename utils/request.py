from base64 import b64decode
from random import choice
from urllib import parse

import requests
from yaml import load, Loader

from infrastructure import log


def create_header(host: str):
    ua = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0"
    ]

    return {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                  "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6,et;q=0.5",
        "Cache-Control": "no-cache",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Host": host,
        "User-Agent": choice(ua)
    }


proxy_data = b64decode(open("/etc/bilibili/proxy.yaml").read()).decode('utf-8')
proxy_config = load(proxy_data, Loader=Loader)
proxy_url = "http://%(username)s:%(password)s@%(host)s:%(port)s" % proxy_config
proxies = {
    "http": proxy_url,
    "https": proxy_url,
}

cookie_text = open("./cookie.txt").read()
cookies = dict([x.strip().split('=') for x in cookie_text.split(";")])


def get(url: str):
    log.info(log.TARGET_HTTP, "Start HTTP request", {"url": url})

    host = parse.urlparse(url).netloc

    try:
        r = requests.get(url, proxies=proxies, headers=create_header(host), cookies=cookies, timeout=1)
        r.encoding = "utf-8"

        log.info(log.TARGET_HTTP, "Finished HTTP request", {"url": url, "status_code": r.status_code})
        return r.text
    except requests.exceptions.RequestException as err:
        log.error(log.TARGET_HTTP, "HTTP get request error", {"url": url, "error": str(err)})
