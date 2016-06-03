FROM python:2.7
MAINTAINER xianlu <xianlubird@gmail.com>
ADD . /test-link
WORKDIR /test-link
# ADD ./sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y --force-yes python-pip
RUN pip install -r requirements.txt
