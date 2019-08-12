import pika

from infrastructure import log


def open_connection():
    conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    chan = conn.channel()

    chan.queue_declare(queue='video_urls')
    return chan


SENDING_CONN = open_connection()


def send(msg):
    log.info(log.TARGET_RABBITMQ, "Sending data to rabbitmq", {"data": msg})
    SENDING_CONN.basic_publish(exchange='', routing_key='video_urls', body=msg)
