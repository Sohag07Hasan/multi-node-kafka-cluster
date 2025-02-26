from kafka import KafkaConsumer
import json
import os

KAFKA_BROKERS = os.getenv('KAFKA_BROKER', 'kafka-1:9092,kafka-2:9092')

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers=KAFKA_BROKERS.split(','),
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Listening for messages...")

for message in consumer:
    print(f"Received: {message.value}")

