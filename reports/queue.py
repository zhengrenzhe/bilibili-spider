import json

import requests

from utils.cfg import get_cfg


def get_queue():
    host = get_cfg("rabbitmq-api.host")
    port = get_cfg("rabbitmq-api.port")
    url = "http://%s:%s/api/queues?page=1&page_size=100&name=&use_regex=false&pagination=true" % (host, port)

    headers = {
        "authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="
    }

    res = requests.get(url, headers=headers)
    return json.loads(res.text)
