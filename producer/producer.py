from kafka import KafkaProducer
import json
import time
import random
import os

KAFKA_BROKERS = os.getenv('KAFKA_BROKER', 'kafka-1:9092,kafka-2:9092')

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKERS.split(','),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'logs'

def generate_log():
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": random.choice(log_levels),
        "message": f"Log message at {time.time()}"
    }

while True:
    log = generate_log()
    producer.send(topic_name, log)
    print(f"Produced: {log}")
    time.sleep(2)

