FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY consumer.py consumer.py

CMD ["python", "consumer.py"]

