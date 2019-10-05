import logging
from typing import Dict

import logstash
from termcolor import colored

from utils.cfg import get_cfg

logger = logging.getLogger("bilibili")
logger.addHandler(logstash.TCPLogstashHandler(host=get_cfg("elk.host"), port=get_cfg("elk.port")))
logger.setLevel(logging.DEBUG)

TARGET_DATABASE = "Database"
TARGET_DAILY_PAGER = "DailyPager"
TARGET_HTTP = "HTTP"
TARGET_RABBITMQ = "RabbitMQ"
TARGET_VIDEO_PAGE = "VideoPage"
TARGET_REDIS = "Redis"
TARGET_CRON = "Cron"


def make_extra(log_target: str, extra: Dict = None):
    _extra = {"log_target": log_target}
    if extra:
        _extra = {**_extra, **extra}
    return _extra


def info(log_target: str, text: str, extra: Dict = None):
    print(colored(text, 'green'))
    logger.info(text, extra=make_extra(log_target, extra))


def warning(log_target: str, text: str, extra: Dict = None):
    print(colored(text, 'yellow'))
    logger.warning(text, extra=make_extra(log_target, extra))


def error(log_target: str, text: str, extra: Dict = None):
    print(colored(text, 'red'))
    logger.error(text, extra=make_extra(log_target, extra))
