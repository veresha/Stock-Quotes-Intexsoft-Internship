FROM python:3.9-slim AS base

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get install make -y \
    && apt-get clean

FROM base AS app

WORKDIR /usr/ExchangeRates

COPY requirements.txt entrypoint-celery.sh /usr/ExchangeRates/
RUN pip install -r requirements.txt

COPY src /usr/ExchangeRates