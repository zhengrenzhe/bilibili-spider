from typing import Dict
import logging

import logstash

logger = logging.getLogger("bilibili")
logger.addHandler(logstash.TCPLogstashHandler(host="localhost", port=5044))
logger.setLevel(logging.DEBUG)


def debug(text: str, extra: Dict = None):
    logger.debug(text, extra=extra)


def info(text: str, extra: Dict = None):
    logger.info(text, extra=extra)


def warning(text: str, extra: Dict = None):
    logger.warning(text, extra=extra)


def error(text: str, extra: Dict = None):
    logger.error(text, extra=extra)


def critical(text: str, extra: Dict = None):
    logger.critical(text, extra=extra)
