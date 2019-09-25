import json

from infrastructure import log, rabbitmq, redis
from jobs import video


def url_job(ch, method, _, body):
    b = json.loads(body)

    log.info(log.TARGET_RABBITMQ, "Get message from rabbitbq", {"content": b})

    if b["type"] == "video":
        url = b["url"]
        if redis.Context.is_visited_today(url):
            log.info(log.TARGET_REDIS, "Video page is visited, ignored", {"url": url})
        else:
            print(b["url"])
            video.do(b["url"])

    ch.basic_ack(delivery_tag=method.delivery_tag)


log.info(log.TARGET_VIDEO_PAGE, "start pages worker...")

conn = rabbitmq.open_connection()
conn.basic_consume(queue='video_urls', on_message_callback=url_job)
conn.start_consuming()
