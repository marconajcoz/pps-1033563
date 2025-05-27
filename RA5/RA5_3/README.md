# 📦 Práctica: Monitorización de un Servidor Linux con Grafana y Prometheus vía Docker 🐳

Esta práctica consiste en desplegar un sistema de monitorización completo utilizando Docker, Prometheus, Node Exporter, cAdvisor y Grafana. El objetivo es visualizar métricas del sistema Ubuntu Server desde un contenedor de Grafana alojado en otra máquina Linux Mint. Ideal para entornos de red segmentados donde el análisis y la observabilidad son claves para la gestión proactiva del sistema. 📊

## 1️⃣ Clonado del repositorio de GitHub 🧬

Se comienza clonando un repositorio de GitHub que contiene un docker-compose.yml preparado con las configuraciones necesarias para levantar los servicios de monitorización: Prometheus, cAdvisor y Grafana.

### 📸 Imagen del clonado del repositorio:

![Clonar Git](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/1-ClonarGitHub.PNG)

## 2️⃣ Construcción del contenedor Docker 🛠️

Una vez clonado el repositorio, se realiza el docker build para construir las imágenes personalizadas que usaremos. En este punto Docker descarga todas las dependencias necesarias y configura el entorno.

### 📸 Imagen del proceso de docker build:

![Docker Build](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/2-BuildDocker.PNG)

## 3️⃣ Levantar los servicios con Docker Compose 🚀

Con las imágenes listas, se ejecuta docker-compose up -d para lanzar los contenedores en segundo plano. Esto inicia automáticamente:

Prometheus (para recopilar métricas 🧠)

cAdvisor (para ver métricas de contenedores 🐳)

Grafana (para visualizar los datos 📊)

### 📸 Imagen de ejecución del comando docker-compose up -d:

![Docker up](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/3-LevantarServicios.PNG)

## 4️⃣, 5️⃣ y 6️⃣ Acceso a los servicios desde el navegador 🌐

Se accede desde un navegador web a los siguientes puertos:

Prometheus: http://localhost:9090

cAdvisor: http://localhost:8080

Grafana: http://localhost:3000

Esto permite verificar que los tres servicios están funcionando correctamente en sus respectivas interfaces web.

### 📸 Capturas de:

Prometheus ✅
![Prometheus](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/4-Prometheus.PNG)

cAdvisor ✅
![cAdvisor](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/5-cAdvisor.PNG)

Grafana ✅
![Grafana](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/6-Grafana.PNG)

## 7️⃣ Verificación de Prometheus en el Ubuntu Server (uServer) 🖥️

En el servidor Ubuntu, también llamado uServer, se instala manualmente Prometheus y Node Exporter. Se comprueba su correcto funcionamiento con el comando:

sudo systemctl status prometheus

### 📸 Imagen del estado activo de Prometheus:

![Prometeus UServer](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/7-PrometheusFuncionaEnUServer.PNG)

## 8️⃣ Acceso remoto a Node Exporter 🌍

Para comprobar que las métricas del uServer están siendo expuestas correctamente, se accede a:

http://192.168.1.85:9100/metrics

Esto confirma que el Node Exporter está activo y sirviendo métricas en la red local, lo cual es esencial para que Prometheus las recopile.

### 📸 Imagen del navegador mostrando las métricas:

![Node Exporter](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/8-MetricasUServer.PNG)

## 9️⃣ Configuración del Data Source en Grafana 📡

Desde el Grafana instalado en el contenedor Docker (corriendo en Linux Mint), se crea una nueva fuente de datos (Data Source) del tipo Prometheus apuntando a la IP del uServer:

http://192.168.1.85:9090

Esta configuración permite que Grafana lea los datos expuestos por Prometheus en el Ubuntu Server remoto.

### 📸 Imagen de configuración del Data Source en Grafana:

![Data Source](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/9-DataSourceHecho.PNG)

## 🔟 Creación del Dashboard en Grafana 📈

Se crea un Dashboard personalizado en Grafana con múltiples paneles que muestran información sobre el estado del sistema uServer, tales como:

Uso de CPU 🧠

Uso de memoria 💾

Esto proporciona una visualización clara y en tiempo real del rendimiento del servidor monitorizado remotamente, gracias a la configuración con el archivo que se encuentra en /assets/code de este repositorio, el [prometheus.yml](https://github.com/marconajcoz/pps-1033563/blob/main/RA5/RA5_3/assets/code/prometheus.yml).

### 📸 Imagen del Dashboard en funcionamiento:

![Dashboard](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_3/assets/images/10-Monitorización.PNG)

✅ Conclusión y objetivos alcanzados 🎯

Gracias al uso de Docker y las herramientas de monitorización (Prometheus, Grafana y Node Exporter), se logró crear un entorno funcional y escalable para observar el estado de un servidor remoto (uServer) desde otro equipo (Linux Mint) de forma gráfica y eficiente. 🧑‍💻
