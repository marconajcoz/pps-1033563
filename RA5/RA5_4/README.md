# Instalación y Despliegue de K3s en Linux Mint (Modo Single-Node) 🚀🐧

En esta guía vamos a instalar **K3s**, una versión ligera y simplificada de Kubernetes, en modo *single-node* sobre Linux Mint. Después desplegaremos un servicio NGINX con dos réplicas y validaremos todo con la herramienta visual **K9s**, que facilita la gestión de clústeres Kubernetes desde la terminal.

---

## 1. Instalación de K3s ⚙️

Para instalar K3s utilizamos el script oficial proporcionado por Rancher Labs. Este script descarga e instala el binario, configura los servicios necesarios y levanta el clúster automáticamente. De esta forma, evitamos pasos manuales complejos y conseguimos un clúster Kubernetes funcional en pocos minutos.

---

*Aquí inserta la imagen del resultado del comando de instalación*  
![Instalación de K3s](ruta/a/tu/imagen1.png)

---

## 2. Verificación del estado del servicio ✅

Una vez instalado, comprobamos que el servicio de K3s esté corriendo correctamente. Esto se hace consultando el estado del servicio mediante el sistema de init de Linux. Si todo está bien, el estado aparecerá como activo y en ejecución, lo que significa que el clúster está listo para usarse.

---

*Aquí inserta la imagen del estado del servicio K3s*  
![Estado del servicio K3s](ruta/a/tu/imagen2.png)

---

## 3. Uso de `kubectl` para administrar el clúster 🖥️

K3s incluye su propia versión integrada de `kubectl`, la herramienta oficial para gestionar Kubernetes. Con ella podemos interactuar con el clúster, listar nodos, desplegar aplicaciones, revisar pods, servicios y más.

Por ejemplo, para listar los nodos y verificar que nuestro nodo está en estado **Ready**, ejecutamos el comando correspondiente.

---

*Aquí inserta la imagen con el listado de nodos*  
![Listado de nodos](ruta/a/tu/imagen3.png)

---

Opcionalmente, podemos configurar el entorno para usar `kubectl` sin necesidad de anteponer `sudo` ni usar el binario propio de K3s. Para ello, copiamos el archivo de configuración a nuestro usuario y creamos un enlace simbólico. Esto facilita el uso de Kubernetes a futuro.

---

## 4. Despliegue de un servicio NGINX con dos réplicas 🐳

Para probar el clúster, creamos un archivo YAML que define un despliegue de NGINX con dos réplicas y un servicio tipo LoadBalancer para exponerlo. Este despliegue hará que dos contenedores NGINX estén corriendo en paralelo dentro del clúster.

Luego aplicamos esta configuración para que Kubernetes cree los pods y el servicio.

---

*Aquí inserta la imagen tras aplicar el despliegue*  
![Aplicar despliegue](ruta/a/tu/imagen4.png)

---

## 5. Validación de los pods y servicios en ejecución 🔍

Es fundamental verificar que los pods se estén ejecutando correctamente y que el servicio esté activo. Con comandos simples podemos listar todos los pods para confirmar su estado y también ver los servicios disponibles para asegurarnos de que NGINX está expuesto y accesible.

---

*Aquí inserta la imagen con el listado de pods*  
![Listado de Pods](ruta/a/tu/imagen5.png)

*Aquí inserta la imagen con el listado de servicios*  
![Listado de Servicios](ruta/a/tu/imagen6.png)

---

## 6. Gestión visual con K9s 🎛️

Para facilitar la administración del clúster, podemos usar **K9s**, una herramienta que muestra una interfaz amigable en la terminal para visualizar recursos, logs y estados del clúster en tiempo real.

Una vez instalado, simplemente lanzamos `k9s` y podremos navegar por todos los recursos con facilidad, haciendo mucho más cómoda la gestión.

---

*Aquí inserta la imagen de K9s en funcionamiento*  
![Interfaz de K9s](ruta/a/tu/imagen7.png)

---

Con estos pasos tendrás un clúster K3s operativo en modo single-node, un servicio NGINX desplegado con réplicas y una forma eficiente de gestionar todo a través de K9s.
