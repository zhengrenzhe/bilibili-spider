import logging
from typing import Dict

import logstash

logger = logging.getLogger("bilibili")
logger.addHandler(logstash.TCPLogstashHandler(host="localhost", port=5044))
logger.setLevel(logging.DEBUG)

TARGET_DATABASE = "Database"
TARGET_DAILY_PAGER = "DailyPager"
TARGET_HTTP = "HTTP"
TARGET_RABBITMQ = "RabbitMQ"


def make_extra(log_target: str, extra: Dict = None):
    _extra = {"log_target": log_target}
    if extra:
        _extra = {**_extra, **extra}
    return _extra


def debug(log_target: str, text: str, extra: Dict = None):
    logger.debug(text, extra=make_extra(log_target, extra))


def info(log_target: str, text: str, extra: Dict = None):
    logger.info(text, extra=make_extra(log_target, extra))


def warning(log_target: str, text: str, extra: Dict = None):
    logger.warning(text, extra=make_extra(log_target, extra))


def error(log_target: str, text: str, extra: Dict = None):
    logger.error(text, extra=make_extra(log_target, extra))


def critical(log_target: str, text: str, extra: Dict = None):
    logger.critical(text, extra=make_extra(log_target, extra))
