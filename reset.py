from infrastructure import redis


def do():
    redis.Context.daily_pager_index = 0
    redis.Context.clear_all_visited()
