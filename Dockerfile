FROM python:3.5

MAINTAINER Nicola Jordan <nic@hixi.ch>

RUN apt-get update && apt-get install -y \
    graphviz \
    graphviz-dev

ADD ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

ADD app /app

WORKDIR /app

CMD python3 manage.py runserver_plus
