FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    curl \
    docker.io \
    unzip \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3

RUN pip install --no-cache-dir pytest

WORKDIR /app

USER jenkins
