import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
chan = conn.channel()

chan.queue_declare(queue='video_urls')


class MQ:
    @staticmethod
    def send(msg: str):
        chan.basic_publish(exchange='', routing_key='video_urls', body=msg)

    @staticmethod
    def register_receive(callback):
        chan.basic_consume(queue='video_urls',
                           auto_ack=True,
                           on_message_callback=callback)
        chan.start_consuming()
