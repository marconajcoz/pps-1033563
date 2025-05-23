# RA5.2 – Automatización de Infraestructura con Terraform, Vagrant y Ansible (Ubuntu 22.04)

## 🎯 Objetivo

El propósito de esta práctica es **automatizar la creación y configuración de una máquina virtual Ubuntu 22.04** usando herramientas de infraestructura como código: **Terraform**, **Vagrant** y **Ansible**.

Se solicita:
- Desplegar una máquina Ubuntu (idealmente 24.04, pero por compatibilidad se ha usado 22.04).
- Instalar el servidor web Apache.
- Crear un archivo `index.html` con el texto `Ansible rocks`.
- Verificar que el contenido sea accesible por HTTP automáticamente.
- Realizar todo el proceso sin intervención manual (totalmente automatizado).

---

## 🧱 Estructura del Proyecto

Esta es la estructura de carpetas que he usado en mi proyecto:

```
TerraformAnsible/
├── Ansible/
│     └── playbook.yml # Playbook con las tareas de configuración
└── Terraform/
    ├── main.tf # Código Terraform con null_resource
    └── Vagrantfile # Configuración de Vagrant + Ansible local
```

Aquí estan los archivos que se han creado para realizar la práctica:

- [`main.tf`](https://github.com/marconajcoz/pps-1033563/blob/main/RA5/RA5_2/assets/code/main.tf) – Configuración de Terraform que ejecuta `vagrant up --provision`.
- [`Vagrantfile`](https://github.com/marconajcoz/pps-1033563/blob/main/RA5/RA5_2/assets/code/Vagrantfile) – Define la máquina virtual, instala Ansible y ejecuta el playbook.
- [`playbook.yml`](https://github.com/marconajcoz/pps-1033563/blob/main/RA5/RA5_2/assets/code/playbook.yml) – Automatiza la instalación y verificación del servidor web Apache.

---

## ⚙️ Proceso Automatizado

### 1. Inicialización de Terraform

Se inicializa Terraform en la carpeta `Terraform/` para preparar el backend y proveedores.

📸 ![Terraform Init](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_2/assets/images/1-TerraformInit.PNG)

---

### 2. Aplicación de la infraestructura

Al ejecutar `terraform apply`, se lanza `vagrant up --provision`, lo que:
- Inicia la máquina virtual
- Instala Ansible
- Ejecuta el playbook automáticamente

📸 ![Terraform Apply](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_2/assets/images/2-TerraformApply.PNG)

---

### 3. Acceso a la máquina virtual

Se puede acceder a la máquina con `vagrant ssh` desde el entorno local:

📸 ![SSH acceso](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_2/assets/images/3-VagrantSSH(acceder).PNG)

---

### 4. Comprobación de IP y sistema operativo

Dentro de la VM se verifica que es Ubuntu 22.04 y que la IP configurada por Vagrant está activa (192.168.56.10):

📸 ![IP y Distro](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_2/assets/images/4-ComprobarIPyDistribución.PNG)

---

### 5. Ejecución automática del Playbook Ansible

El playbook `playbook.yml` realiza las siguientes tareas:
- Actualiza e instala paquetes (`apt update/upgrade`)
- Instala `apache2`
- Crea un archivo `/var/www/html/index.html` con contenido `"Ansible rocks"`
- Reinicia Apache
- Ejecuta un `curl localhost` para validar que el contenido se sirve correctamente

📸 ![Playbook en ejecución](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_2/assets/images/5-DemostraciónPlaybookEjecutado.PNG)

---

### 6. Validación final de Apache

Se comprueba desde dentro de la VM con `curl` que el contenido web es el esperado:

📸 ![Comprobación curl](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_2/assets/images/6-ComprobarApacheFunciona.PNG)

---

## ✅ Conclusión

La práctica se ha completado con éxito. El sistema:

- ✅ Lanza automáticamente una máquina Ubuntu 22.04  
- ✅ Configura un servidor web sin intervención manual  
- ✅ Verifica su funcionamiento desde el mismo playbook  

Este flujo representa un entorno totalmente automatizado de CI para servidores de desarrollo o pruebas, alineado con los principios de **Infraestructura como Código**.
