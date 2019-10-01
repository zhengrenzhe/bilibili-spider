from infrastructure import postgres, redis, log

log.info(log.TARGET_REDIS, "Set visited videos list")

vids = postgres.video.get_all_vids()
for v in vids:
    redis.Context.visit(str(v[0]))

log.info(log.TARGET_REDIS, "Set visited videos list finished")
