from os import path

import requests

from utils.yaml import read_yaml

cfg = read_yaml(path.normpath(path.join(path.dirname(__file__), '../slack.yaml')))


def send_msg(text: str):
    res = requests.post(url=cfg.get("webhook"), json={"text": text})
    return res.status_code == 200
