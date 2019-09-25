import logging
from typing import Dict

import logstash

logger = logging.getLogger("bilibili")
logger.addHandler(logstash.TCPLogstashHandler(host="elk-inside-service", port=5044))
logger.setLevel(logging.DEBUG)

TARGET_DATABASE = "Database"
TARGET_DAILY_PAGER = "DailyPager"
TARGET_HTTP = "HTTP"
TARGET_RABBITMQ = "RabbitMQ"
TARGET_VIDEO_PAGE = "VideoPage"
TARGET_REDIS = "Redis"


def make_extra(log_target: str, extra: Dict = None):
    _extra = {"log_target": log_target}
    if extra:
        _extra = {**_extra, **extra}
    return _extra


def info(log_target: str, text: str, extra: Dict = None):
    print(text)
    logger.info(text, extra=make_extra(log_target, extra))


def warning(log_target: str, text: str, extra: Dict = None):
    print(text)
    logger.warning(text, extra=make_extra(log_target, extra))


def error(log_target: str, text: str, extra: Dict = None):
    print(text)
    logger.error(text, extra=make_extra(log_target, extra))
