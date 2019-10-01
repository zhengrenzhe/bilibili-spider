import redis

from infrastructure import log

cfg_db = redis.Redis(host="redis-service", port=6379, db=0)
visited_db = redis.Redis(host="redis-service", port=6379, db=1)


def update(name, value):
    cfg_db.set(name, value)
    log.info(log.TARGET_REDIS, "Redis update key:%s value:%s" % (name, value))


def get(name):
    value = cfg_db.get(name)
    log.info(log.TARGET_REDIS, "Redis get key:%s value:%s" % (name, value))
    return value and value.decode("utf-8")


class _Context:
    @property
    def daily_pager_index(self):
        return int(get("daily_pager_index") or 0)

    @daily_pager_index.setter
    def daily_pager_index(self, new_index):
        update("daily_pager_index", new_index)

    @staticmethod
    def is_visited(key=""):
        return visited_db.get(key) == b'1'

    @staticmethod
    def visit(key=""):
        visited_db.set(key, 1)


Context = _Context()
