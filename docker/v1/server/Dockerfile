FROM python:3.8.5-slim

WORKDIR /server
COPY . /server

RUN apt-get update -y \
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/* \
    && python3 setup.py install

CMD python v1/server.py
