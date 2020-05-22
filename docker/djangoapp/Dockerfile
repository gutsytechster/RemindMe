FROM python:3.6.9-slim

RUN apt-get update && apt-get install -y gcc=4:8.3.0-1 libpq-dev=11.7-0+deb10u1 && rm -rf /var/lib/apt/lists/*
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 0
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r /app/requirements.txt
