import os, pika, json
from dotenv import load_dotenv


load_dotenv(os.path.join(os.getcwd(), '.env'))
AMQP = os.getenv('AMQP')

params = pika.URLParameters(AMQP)
connection = pika.BlockingConnection(params)
channel = connection.channel()

print('start publish')

def publish(method, body):
    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
