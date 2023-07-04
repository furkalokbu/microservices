import pika

params = pika.URLParameters('amqps://oospddyd:8smUeB1YmqROPB57IB-9abtbp_4AGj8A@sparrow.rmq.cloudamqp.com/oospddyd')
connection = pika.BlockingConnection(params)
channel = connection.channel()

print('start publish')

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='Hello Main')
