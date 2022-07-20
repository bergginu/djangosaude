# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
  # Dep. do Python
  && apt-get install -y build-essential \
  # Dep. do psycopg2
  && apt-get install -y libpq-dev \
  # Dep. Adicionais
  && apt-get install -y telnet netcat \
  # Limpando a cache, temporarios, auxiliares do apt.
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./dj /app/
