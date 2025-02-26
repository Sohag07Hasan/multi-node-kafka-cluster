# 🐳 Multi-Node Kafka Cluster with Zookeeper

This project sets up a **multi-broker Apache Kafka cluster** with **Zookeeper**, a **producer**, and a **consumer** using **Docker Compose**. It allows for **fault-tolerant message streaming** across brokers.

## 🚀Features

✅ Multi-node **Kafka cluster** (2 brokers).  
✅ **Zookeeper** for broker coordination.  
✅ **Kafka Producer** for log generation.  
✅ **Kafka Consumer** for log consumption.  
✅ **Load balancing discussion** for scaling strategies.

## ⚡ Getting Started  

### 📌 1. Prerequisites
Ensure you have Docker and Docker Compose installed on your system.

#### 
```bash
# Install Docker
sudo apt update && sudo apt install docker.io -y

# Install Docker Compose
sudo apt install docker-compose -y
```
### 📌 2. Clone the Repository
 
```bash
git clone https://github.com/your-username/kafka-multi-node-docker.git
```

### 📌 3. Start the Kafka Cluster
```bash
cd kafka-multi-node-docker
docker-compose up -d --build
```
This will start
- 1 Zookeeper instance
- 2 Kafka brokers
- 1 Producer
- 1 Consumer

### 📌 4. Verify the Setup
Check if Kafka brokers are running:
```bash
docker ps
```

Check if topics are created:
```bash
docker exec -it kafka-1 kafka-topics --list --bootstrap-server kafka-1:9092
```

### 📌 5. Monitor Producer and Consumer
#### 🔹 Check Producer Logs
```bash
docker logs -f kafka_producer
```

#### 🔹 Check Consumer Logs
```bash
docker logs -f kafka_producer
```

## 📜 Project Structure
```bash
multi-node-kafka-cluster/
│── docker-compose.yml  # Defines all services (Kafka, Zookeeper, Producer, Consumer)
│── producer/
│   ├── Dockerfile
│   ├── producer.py     # Python script to generate logs
│   ├── requirements.txt
│── consumer/
│   ├── Dockerfile
│   ├── consumer.py     # Python script to consume logs
│   ├── requirements.txt
└── README.md
```

## 🔗 References
- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Kafka Python Client (kafka-python)](https://github.com/dpkp/kafka-python)
- [A Simple Kafka and Python Walkthrough](https://github.com/quixio/simple-kafka-python)
- [Kafka Tutorial for Beginners](https://www.youtube.com/watch?v=QkdkLdMBuL0&list=LL)



## 🤝 Contributing
Feel free to fork this repo, raise issues, or submit PRs! 😊


## 📜 License
This project is licensed under the
[MIT](https://choosealicense.com/licenses/mit/)
License.
