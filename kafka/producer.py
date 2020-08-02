from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.99.100:9092")

print(client.topics)

topic = client.topics['my.test']

with topic.get_sync_producer() as producer:
    for i in range(4):
        producer.produce(('test message ' + str(i ** 2)).encode())