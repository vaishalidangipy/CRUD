FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY ./requirments.txt /
RUN apk update \
    && apk add bash \
    && apk add --virtual build-deps gcc python3-dev \
    && apk add --no-cache --virtual .build-deps gcc musl-dev \
    && apk add git \
    && apk add --no-cache mariadb-dev
RUN apk del build-deps
COPY . .
RUN pip install -r requirments.txt
EXPOSE 8000
