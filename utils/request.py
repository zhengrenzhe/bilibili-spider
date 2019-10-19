import json
import sys
from os import path
from urllib import parse

import requests

from infrastructure import log
from utils.http_header import create_header
from utils.yaml import read_yaml

proxies = None

if "--no-proxy" not in sys.argv:
    proxy_config_path = path.normpath(path.join(path.dirname(__file__), '../proxy.yaml'))
    proxy_config = read_yaml(proxy_config_path)
    proxy_url = "http://%(username)s:%(password)s@%(host)s:%(port)s" % proxy_config
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

cookie_text = open(path.normpath(path.join(path.dirname(__file__), '../cookies'))).read()
cookies = dict(map(lambda x: x.strip().split('='), cookie_text.split(";")))


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


wechat_headers = {
    "Host": "api.bilibili.com",
    "Content-Type": "application/json",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Mobile/15E148 MicroMessenger/7.0.7(0x17000721) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx7564fd5313d24844/90/page-frame.html",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate, br"
}


def api_get(url: str):
    try:
        r = requests.get(url, proxies=proxies, timeout=2, headers=wechat_headers)
        r.encoding = "utf-8"

        res = json.loads(r.text)

        if res.get("code") == 0:
            log.info(log.TARGET_HTTP, "API get success", {"url": url})
            return True, res.get("data")
        else:
            log.error(log.TARGET_HTTP, "API get error",
                      {"url": url, "error_msg": res.get("message"), "error_code": res.get("code")})
            return False, res.get("message")

    except requests.exceptions.RequestException as err:
        log.error(log.TARGET_HTTP, "API network error", {"url": url, "error": str(err)})
        return False, "Proxy Error"

    except json.JSONDecodeError as err:
        log.error(log.TARGET_OTHER, "JSON Parse error", {"url": url, "error": str(err)})
        return False, "JSON Error"
