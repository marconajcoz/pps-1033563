# 5.1 Instalación y Despliegue de K3s y visión con K9S (Modo Single-Node) 🚀🐧

En esta guía vamos a instalar **K3s**, una versión ligera y simplificada de Kubernetes, en modo *single-node* sobre Linux Mint. Después desplegaremos un servicio NGINX con dos réplicas y validaremos todo con la herramienta visual **K9s**, que facilita la gestión de clústeres Kubernetes desde la terminal.

---

## 1. Instalación de K3s ⚙️

Para instalar K3s utilizamos el script oficial proporcionado por Rancher Labs. Este script descarga e instala el binario, configura los servicios necesarios y levanta el clúster automáticamente. De esta forma, evitamos pasos manuales complejos y conseguimos un clúster Kubernetes funcional en pocos minutos.

---
 
![K3S](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/1-InstalarK3S.PNG)

---

## 2. Verificación del estado del servicio ✅

Una vez instalado, comprobamos que el servicio de K3s esté corriendo correctamente. Esto se hace consultando el estado del servicio mediante el sistema de init de Linux. Si todo está bien, el estado aparecerá como activo y en ejecución, lo que significa que el clúster está listo para usarse.

---

![K3S Status](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/2-StatusK3S.PNG)

---

## 3. Uso de `kubectl` para administrar el clúster 🖥️

K3s incluye su propia versión integrada de `kubectl`, la herramienta oficial para gestionar Kubernetes. Con ella podemos interactuar con el clúster, listar nodos, desplegar aplicaciones, revisar pods, servicios y más.

Por ejemplo, para listar los nodos y verificar que nuestro nodo está en estado **Ready**, ejecutamos el comando correspondiente.

---

![K3S Nodos](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/3-NodoListo.PNG)

---

Opcionalmente, podemos configurar el entorno para usar `kubectl` sin necesidad de anteponer `sudo` ni usar el binario propio de K3s. Para ello, copiamos el archivo de configuración a nuestro usuario y creamos un enlace simbólico. Esto facilita el uso de Kubernetes a futuro.

---

## 4. Despliegue de un servicio NGINX con dos réplicas 🐳

Para probar el clúster, creamos un archivo [YAML que define un despliegue de NGINX](https://github.com/marconajcoz/pps-1033563/blob/main/RA5/RA5_4/assets/code/nginx-deployment.yaml) accesible en /assets/code de este repositorio con dos réplicas y un servicio tipo LoadBalancer para exponerlo. Este despliegue hará que dos contenedores NGINX estén corriendo en paralelo dentro del clúster.

Luego aplicamos esta configuración para que Kubernetes cree los pods y el servicio.

---

![Nginx Deploy](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/4-AplicarNginxDeploy.PNG)

---

## 5. Validación de los pods y servicios en ejecución 🔍

Es fundamental verificar que los pods se estén ejecutando correctamente y que el servicio esté activo. Con comandos simples podemos listar todos los pods para confirmar su estado y también ver los servicios disponibles para asegurarnos de que NGINX está expuesto y accesible.

---

![Pods K3S](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/5-ComprobarNodos.PNG)

---

## 6. Gestión visual con K9s 🎛️

Para facilitar la administración del clúster, podemos usar **K9s**, una herramienta que muestra una interfaz amigable en la terminal para visualizar recursos, logs y estados del clúster en tiempo real.

Una vez instalado, simplemente lanzamos `k9s` y podremos navegar por todos los recursos con facilidad, haciendo mucho más cómoda la gestión.

---

![K9S Funciona](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/7-NodosDesdeK9S.PNG)

---

Con estos pasos tendrás un clúster K3s operativo en modo single-node, un servicio NGINX desplegado con réplicas y una forma eficiente de gestionar todo a través de K9s.

# 5.2 Instalación y Despliegue de K3s y visión con K9S (Modo HA) 🚀🐧

## 🚀 Introducción

Kubernetes es una plataforma de orquestación de contenedores que automatiza la implementación, escalado y gestión de aplicaciones en contenedores. Una de sus capacidades más importantes es la alta disponibilidad (HA), que permite mantener las aplicaciones funcionando incluso si uno o varios nodos del clúster fallan.

En esta práctica se ha desplegado un clúster Kubernetes en alta disponibilidad usando K3s, una distribución ligera y certificada de Kubernetes diseñada para entornos con recursos limitados, pero con todas las funcionalidades esenciales.

## 💻 Entorno utilizado

Se han empleado tres servidores con Ubuntu Server 24.04, configurados para formar un clúster K3s en alta disponibilidad. Los nodos se identifican como master1k3s, master2k3s y master3k3s.  

Cada nodo está configurado para que el primero (master1k3s) actúe como nodo principal (control-plane), y los otros dos se unan al clúster utilizando el token generado por el primero.

---

## 🛠️ Pasos realizados

### 1️⃣ Instalación en master1k3s y obtención del token

En el nodo master1k3s se instaló K3s como nodo principal. Tras la instalación, se extrajo el token necesario para que los demás nodos puedan unirse al clúster con alta disponibilidad. Este token permite autenticar y conectar de forma segura los nodos adicionales.

![K3S Master1](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/8-InstalarK3SAltaDisp.PNG)

### 2️⃣ Instalación en master2k3s y master3k3s con referencia al token de master1k3s

En los nodos master2k3s y master3k3s se instaló K3s como nodos adicionales, especificando durante la instalación el token obtenido de master1k3s y la IP del nodo principal. Esto hizo posible la unión de los nodos al clúster, configurando así un entorno con múltiples nodos que ofrecen resiliencia y balanceo de carga para los componentes de control.

![K3S Master2](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/9-InstalarK3SyLinkMast1EnMast2.PNG)

![K3S Master3](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/10-InstalarK3SyLinkMast1EnMast3.PNG)

### 3️⃣ Verificación del clúster con `kubectl get nodes`

Desde cualquiera de los nodos con la configuración correcta del fichero kubeconfig, se ejecutó el comando para listar los nodos del clúster. Se pudo comprobar que los tres nodos aparecen como listos (`Ready`), donde master1k3s figura con el rol de `control-plane,etcd,master` y master2k3s y master3k3s aparecen con estado listo pero sin roles explícitos de control-plane, lo cual es correcto para un clúster K3s configurado para HA.

![Nodos](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/11-3Nodos.PNG)

### 4️⃣ Creación y despliegue de nginx-deployment

Se creó un fichero [nginx-deployment.yaml](https://github.com/marconajcoz/pps-1033563/blob/main/RA5/RA5_4/assets/code/nginx-deployment.yaml) que define un despliegue con varias réplicas del servidor web Nginx. Con el comando `kubectl apply -f nginx-deployment.yaml` se aplicó esta configuración al clúster, creando el deployment y el servicio asociado.

![Aplicar Nginx](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/12-AplicarNginxMaster1.PNG)

### 5️⃣ Comprobación de los pods y servicios

Se verificó que los pods del despliegue de Nginx se estaban ejecutando correctamente usando `kubectl get pods`. Se observaron dos réplicas, ambas en estado `Running`, distribuidas en dos nodos distintos (master2k3s y master3k3s). Esto indica que el clúster está gestionando el despliegue de forma distribuida.

El servicio asociado se creó como tipo `LoadBalancer` con un puerto expuesto, aunque en un entorno local el EXTERNAL-IP aparece como `<pending>`, esto es esperado si no hay un controlador externo que asigne IPs públicas.

![Pods y SVC](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/13-PodsYSVCMaster1.PNG)

### 6️⃣ Prueba de acceso con curl a Nginx

Se realizó una consulta HTTP directa al puerto del servicio expuesto (por ejemplo, en la IP 192.168.1.121 con puerto 31002), y se recibió la página estándar de bienvenida de Nginx. Esto confirma que el servidor web está corriendo correctamente dentro del clúster y es accesible desde la red.

![Curl Nginx](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/14-NginxFunciona.PNG)

### 7️⃣ Monitorización visual con K9s

Finalmente, se utilizó la herramienta K9s para visualizar el estado del clúster de manera interactiva. En K9s se pudieron observar los pods desplegados, sus estados, nodos en los que se ejecutan, consumo de recursos y más. La visualización confirma que las réplicas de nginx están distribuidas en nodos diferentes, reforzando la arquitectura de alta disponibilidad.

![K9S](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_4/assets/images/15-HAConseguidaK9S.PNG)
