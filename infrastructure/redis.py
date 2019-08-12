import redis

import log

r = redis.Redis()


def update(name, value):
    r.set(name, value)
    log.info("Redis update key:%s value:%s" % (name, value))


def get(name):
    value = r.get(name)
    log.info("Redis get key:%s value:%s" % (name, value))
    return value.decode("utf-8")


class _Context:
    @property
    def daily_pager_index(self):
        return int(get("daily_pager_index")) or 0

    @daily_pager_index.setter
    def daily_pager_index(self, new_index):
        update("daily_pager_index", new_index)


Context = _Context()
