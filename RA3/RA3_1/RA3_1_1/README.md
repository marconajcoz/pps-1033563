# Práctica 1: Dockerfile, CSP y Certificados  
Esta sección corresponde a las siguientes imagenes.  
[Imagen justo después del build](https://hub.docker.com/repository/docker/marnajcoz/practicas/tags/apache-hardening/sha256-917ea5b8c7ae3e0f3ce4f9ea6f4c509fb0eb2432145e75c40ac361658c2e3092)  
[Imagen con CSP aplicado](https://hub.docker.com/repository/docker/marnajcoz/practicas/tags/csp/sha256-628fcd05df7b16530ac689e5fa79318eec82374276376d1764c4bc5b910731f6)  

## Dockerfile  
Este es el archivo Dockerfile a partir del que se ha realizado el docker y toda la práctica:  
![IMG](https://github.com/marconajcoz/pps-1033563/blob/main/RA3/RA3_1/RA3_1_1/assets/1-DockerfileInicial.PNG)  

## CSP  
Vamos a deshabilitar el autoindex:  
![IMG](https://github.com/marconajcoz/pps-1033563/blob/main/RA3/RA3_1/RA3_1_1/assets/2-DeshabilitarAutoindex.PNG)  

Continuando con introducir el ServerToken:  
![IMG](https://github.com/marconajcoz/pps-1033563/blob/main/RA3/RA3_1/RA3_1_1/assets/3-ServerToken.PNG)  

Se aplica el header en modo estricto:  
![IMG](https://github.com/marconajcoz/pps-1033563/blob/main/RA3/RA3_1/RA3_1_1/assets/4-HEaderEstricto.PNG)  

Y comprobamos que el CSP funciona sacando la cabezera con un curl:  
![IMG](https://github.com/marconajcoz/pps-1033563/blob/main/RA3/RA3_1/RA3_1_1/assets/7-CSPFunciona.PNG)  

## Certificados  
Vamos a crear certificados autofirmados para cifrar las comunicaciones, necesario para realización del resto de ejercicios:  
![IMG](https://github.com/marconajcoz/pps-1033563/blob/main/RA3/RA3_1/RA3_1_1/assets/5-Certificados.PNG)  

Ahora que tenemos los certificados creados, vamos a crear el Virtualhost 443 para recibir conexiones seguras, y a redirigir las del puerto 80 al 443.  
![IMG](https://github.com/marconajcoz/pps-1033563/blob/main/RA3/RA3_1/RA3_1_1/assets/6-Redirigir443.PNG)
