import collections
from hashlib import md5
from os import path

from utils.yaml import read_yaml


def get_video_data(vid: str):
    auth = read_yaml(path.normpath(path.join(path.dirname(__file__), '../auth.yaml')))
    auth["aid"] = vid

    ordered = dict(collections.OrderedDict(sorted(auth.items())))

    queries = "&".join(["%s=%s" % (k, v) for k, v in ordered.items()])

    h = md5()
    h.update((queries + "27eb53fc9058f8c3").encode("utf-8"))
    print(h.hexdigest())

    # queries += "&sign=98065c207113f96f40a819ad33dc3621"

    # crypto = md5()
    # crypto.update(query_string.encode('utf-8'))
    # print(query_string)
    # print(crypto.hexdigest())
    # hash.(query_string)

    # url = "https://app.bilibili.com/x/v2/view?%s" % queries
    # print(api_get(url)[0])
