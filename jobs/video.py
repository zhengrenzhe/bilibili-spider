import json

from infrastructure import log, rabbitmq, redis
from parse import parse_video_page


def do(url: str):
    redis.Context.visit(url)

    log.info(log.TARGET_VIDEO_PAGE, "Start new video page url job", {"url": url})

    suc, video_base, video_increment, video_related = parse_video_page(url)

    if not suc:
        log.error(log.TARGET_VIDEO_PAGE, "Failer to fetch video page data", {"url": url})
        return

    video_base.save()
    video_increment.save()
    video_related.save()

    for r_vid in video_related.related_vid:
        r_url = "https://www.bilibili.com/video/av%s" % r_vid
        if not redis.Context.is_visited(r_url):
            rabbitmq.send(json.dumps({"type": "video", "url": r_url}))
            log.info(log.TARGET_VIDEO_PAGE, "Add related video to queue", {"url": r_url})

    log.info(log.TARGET_VIDEO_PAGE, "Finished new video page url job", {"url": url})


if __name__ == "__main__":
    do("https://www.bilibili.com/video/av48401550?spm_id_from=333.334.b_62696c695f646f756761.5")
