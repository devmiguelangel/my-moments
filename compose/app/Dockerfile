FROM python:3.12-alpine

RUN apk update && \
  apk add --no-cache \
    gcc \
    python3-dev \
    bash

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./auth-service/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./compose/app/start.sh /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

CMD [ "/start" ]
