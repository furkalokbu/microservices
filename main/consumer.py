import os, pika
from dotenv import load_dotenv


load_dotenv(os.path.join(os.getcwd(), '.env'))
AMQP = os.getenv('AMQP')

params = pika.URLParameters(AMQP)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print(f'{body}')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
