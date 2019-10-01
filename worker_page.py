import json

from infrastructure import log, rabbitmq
from process import process_video


def spider_job(ch, method, _, body):
    b = json.loads(body)

    if b["type"] == "video":
        process_video(b["url"])

    ch.basic_ack(delivery_tag=method.delivery_tag)


log.info(log.TARGET_VIDEO_PAGE, "start pages worker...")

conn = rabbitmq.open_connection()
conn.basic_consume(queue='video_urls', on_message_callback=spider_job)
conn.start_consuming()
