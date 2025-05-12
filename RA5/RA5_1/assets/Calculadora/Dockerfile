FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    curl \
    unzip \
    docker.io

WORKDIR /app

USER jenkins
