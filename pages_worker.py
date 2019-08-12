import json

from infrastructure import log
from infrastructure import rabbitmq
from jobs import video


def url_job(ch, method, properties, body):
    b = json.loads(body)

    log.info(log.TARGET_RABBITMQ, "Get message from rabbitbq", {"content": b})

    if b["type"] == "video":
        print(b["url"])
        video.do(b["url"])


conn = rabbitmq.open_connection()
conn.basic_consume(queue='video_urls', auto_ack=True, on_message_callback=url_job)
conn.start_consuming()
