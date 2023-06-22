FROM tiangolo/uvicorn-gunicorn-fastapi:latest

RUN apt-get update && \
    apt-get install -y postgresql-client

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt
