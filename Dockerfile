FROM python:2.7
MAINTAINER niusmallnan <niusmallnan@gmail.com>

ENV SOURCE_REPO https://github.com/niusmallnan/cloudx5-benchmark.git

RUN mkdir /root/.pip
COPY .pip.aliyun.conf /root/.pip/pip.conf
COPY .jessie.source.list /etc/apt/sources.list

RUN mkdir -p /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        apache2-utils \
        git \
        && rm -rf /var/lib/apt/lists/* \
        && git clone $SOURCE_REPO \
        && cd cloudx5-benchmark \
        && pip install -r requirements.txt \
        && python setup.py develop

CMD ["/bin/bash"]
