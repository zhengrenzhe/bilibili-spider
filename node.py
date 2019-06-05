import pika
import time

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()


# channel.queue_declare(queue='task_queue')


def cb(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='task_queue', on_message_callback=cb)

channel.start_consuming()
