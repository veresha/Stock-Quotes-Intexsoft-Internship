FROM python:3.9-slim AS base

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get install make -y \
    && apt-get clean

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM base AS app

WORKDIR /usr/ExchangeRates

COPY entrypoint-celery.sh /usr/ExchangeRates/

COPY src /usr/ExchangeRates