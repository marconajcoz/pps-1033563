FROM jenkins/jenkins:lts

USER root

# Instala Docker dentro del contenedor
RUN apt-get update && apt-get install -y docker.io

# Regresa al usuario Jenkins
USER jenkins
