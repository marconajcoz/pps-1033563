FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    docker.io \
    curl \
    unzip \
    && pip3 install --no-cache-dir pytest

WORKDIR /app

USER jenkins
