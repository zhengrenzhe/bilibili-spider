import json

from infrastructure import rabbitmq
from jobs import video


def url_job(ch, method, properties, body):
    b = json.loads(body)

    if b["type"] == "video":
        print(b["url"])
        video.work(b["url"])


conn = rabbitmq.open_connection()
conn.basic_consume(queue='video_urls', auto_ack=True, on_message_callback=url_job)
conn.start_consuming()
