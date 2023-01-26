#syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
LABEL maintainer="eg.shuraev@gmail.com"
LABEL description="This file contains instructions for \
creating an image for the Ip-manager project."
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["./launch.sh"]
