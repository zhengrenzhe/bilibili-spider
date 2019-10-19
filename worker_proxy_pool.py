from proxy_pool.check import check_proxy_available
from proxy_pool.fetcher import fetch_goubanjia

RULES = [
    {
        "name": "goubanjia",
        "url": "http://www.goubanjia.com",
        "pager": None,
        "pager_interval": 60 * 10,
        "fetcher": fetch_goubanjia
    }
]

if __name__ == "__main__":
    # ps = fetch_goubanjia()
    # for p in ps:
    #     print("check: %s" % p)
    #     print(check_proxy_available(p))

    print(check_proxy_available("39.106.223.134:8305"))
