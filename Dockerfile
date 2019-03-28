FROM python:3.7-slim
LABEL maintainer="bcgalvin@gmail.com"

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

ARG BUILD_DEPS="freetds-dev libkrb5-dev libssl-dev libffi-dev libpq-dev git"
ARG APT_DEPS="libsasl2-dev freetds-bin build-essential default-libmysqlclient-dev apt-utils curl rsync netcat locales"

COPY . /opt/koala/
WORKDIR /opt/koala

RUN set -euxo pipefail \
    && apt update \
    && if [ -n "${BUILD_DEPS}" ]; then apt install -y $BUILD_DEPS; fi \
    && pip install --no-cache-dir --upgrade pip==19.0.1 \
    && apt purge --auto-remove -yqq $BUILD_DEPS \
    && apt autoremove -yqq --purge \
    && apt clean

CMD ["/bin/bash"]
