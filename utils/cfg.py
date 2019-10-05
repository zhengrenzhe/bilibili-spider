import json
from os import path

services_config_path = path.normpath(path.join(path.dirname(__file__), '../services.json'))
services_content = json.load(open(services_config_path))


def get_cfg(key_path: str):
    key_path = key_path.split(".")
    s = services_content
    for k in key_path:
        s = s.get(k, {})
    return s
