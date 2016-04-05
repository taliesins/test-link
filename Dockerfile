FROM python:2.7
MAINTAINER xianlu <xianlubird@gmail.com>
ADD ./test-link
WORKDIR /test-link
RUN apt-get update && apt-get install -y python-pip
RUN pip install -r requirements.txt
