from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.99.100:9092")

print(client.topics)

topic = client.topics['my.test']

consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print(message.offset, message.value)