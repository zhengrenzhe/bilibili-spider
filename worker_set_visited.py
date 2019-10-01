from infrastructure import postgres, redis

vids = postgres.video.get_all_vids()
for v in vids:
    redis.Context.visit(str(v[0]))
