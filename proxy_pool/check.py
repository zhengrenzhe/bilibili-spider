import json

import requests

from utils.http_header import create_header


def check_proxy_available(proxy: str) -> (bool, int):
    proxies = {
        "http": proxy,
        "https": proxy
    }

    target = "http://api.bilibili.com/x/web-interface/view/detail?aid=%s" % "71493720"

    check_res = requests.get(target, headers=create_header("api.bilibili.com"), proxies=proxies, timeout=1)
    check_res.encoding = "utf-8"

    try:
        j = json.loads(check_res.content)
        if j.get("code") == 0:
            return True, -1
        return False, 1
    except requests.exceptions.ProxyError as err:
        return False, 0
    except json.JSONDecodeError as err:
        return False, 1
