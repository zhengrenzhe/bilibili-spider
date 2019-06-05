import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='task_queue', durable=True)

channel.basic_publish(exchange='', routing_key='task_queue', body='fuckfuckfuckfuckfuckfuck',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

conn.close()
