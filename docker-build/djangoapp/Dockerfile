FROM python:3.6.9-slim

RUN apt-get update && apt-get install -y gcc=4:8.3.0-1 libpq-dev=11.7-0+deb10u1 && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

WORKDIR /app
COPY ./src/ /app
