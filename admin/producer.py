import pika, json

params = pika.URLParameters('')
connection = pika.BlockingConnection(params)
channel = connection.channel()

print('start publish')

def publish(method, body):
    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
