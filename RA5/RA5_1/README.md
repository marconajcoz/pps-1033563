# Práctica RA5.1: CI/CD con Jenkins y Python

## 🔪 Proyecto: Calculadora en Python con Jenkins

Este proyecto forma parte de la práctica RA5.1 del módulo de Ciberseguridad, donde se implementa una **pipeline de integración continua** usando **Jenkins**, integrando un script de Python y pruebas unitarias automatizadas.

---

## 📁 Estructura del proyecto

```
RA5_1/
└── assets/
    └── Calculadora/
        ├── calculadora.py
        ├── test_calculadora.py
        ├── Jenkinsfile
        ├── jenkinsfile.docker
        ├── Dockerfile
        ├── docker-compose.yml
        └── README.md
```

---

## 📊 Implementación de la Calculadora en Python

El proyecto comienza con la creación de un script en Python que implementa una clase `Calculadora` con un método `multiplicar`. Esta clase se prueba desde la línea de comandos y mediante pruebas unitarias.

A continuación se muestra el código fuente funcional:

![Código Python](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/1-Calculadora.PNG)

Para garantizar que el código funciona correctamente, se han creado pruebas automáticas con `unittest`, como se observa en la siguiente imagen:

![Unittest funcionando](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/2-UniTest.PNG)

---

## ⚙️ Jenkinsfile

Se define una pipeline de Jenkins que clona el repositorio y ejecuta los tests unitarios con `unittest`.

### Ejemplo de pipeline:

```groovy
pipeline {
    agent any
    triggers {
        pollSCM('* * * * *') // Detecta cambios en el repositorio cada minuto
    }
    stages {
        stage('Clonar repo') {
            steps {
                git 'https://github.com/marconajcoz/pps-1033563.git'
            }
        }
        stage('Ejecutar tests') {
            steps {
                dir('RA5/RA5_1/assets/Calculadora') {
                    sh 'python3 -m unittest test_calculadora.py'
                }
            }
        }
    }
}
```

---

## 🚣 Jenkins con Docker

Para facilitar la configuración del entorno de integración continua, se ha optado por levantar Jenkins mediante Docker.

Primero, se ejecuta el siguiente comando:

```bash
docker-compose build
docker-compose up -d
```

Esto lanza Jenkins en `http://localhost:8080`:

![Jenkins con Docker](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/3-PuestaEnMarcha.PNG)

Una vez que el contenedor está en marcha, se recupera la contraseña inicial con:

```bash
docker exec -it jenkins_jenkins_1 cat /var/jenkins_home/secrets/initialAdminPassword
```

![Contraseña inicial Jenkins](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/4-ContraseñaTemporal.PNG)

Tras introducirla en el navegador, Jenkins solicita crear el primer usuario administrador e instalar los plugins recomendados:

![Plugins Jenkins](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/5-InstalarPlugins.PNG)

Finalmente, accedemos al panel de Jenkins ya funcional:

![Jenkins activo](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/6-JenkinsActivo.PNG)

---

🔍 Configuración de la pipeline y credenciales

Paso 1: Crear la tarea tipo Pipeline en Jenkins

Desde el panel principal de Jenkins, seleccionamos "Nuevo Item" y creamos una tarea tipo "Pipeline", que nos permitirá definir todas las etapas desde el código.

![CrearPipeline](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/7-CrearPipeline.PNG)

Paso 2: Crear un token personal (PAT) para GitHub

Para que Jenkins pueda acceder al repositorio privado de GitHub, creamos un token personal desde la configuración de GitHub. Este token debe tener permisos sobre repo y workflow.

![TokenGitHub](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/8-TokenGitHub.PNG)

Paso 3: Asociar el token en Jenkins como credencial

Una vez generado el token, se añade en Jenkins desde Administrar Jenkins > Credenciales > Global. Se selecciona el tipo Username with password y se introduce el nombre de usuario de GitHub y el token como contraseña.

![Insertar Token](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/9-PonerToken.PNG)

Paso 4: Configurar la tarea con SCM y script path

En la configuración del proyecto, indicamos la URL del repositorio y seleccionamos la credencial previamente añadida. También se define la rama a utilizar (main) y se deja activado el uso de Jenkinsfile por defecto.

![Configuracion pipeline](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/10-Configuracion.PNG)

Paso 5: Visualización de la pipeline ejecutándose

Una vez lanzada la pipeline, Jenkins representa gráficamente la ejecución de cada etapa. Si alguna falla, se marca con una cruz. En este ejemplo se ve el proceso completo: desde el checkout hasta la ejecución de Docker Compose.

![Error](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/11-Error.PNG)

---

## 🔬 Tests

Los tests unitarios están implementados con `unittest` y verifican el método de multiplicación de la clase `Calculadora`.

### `test_calculadora.py` (fragmento):

```python
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_multiplicacion(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(3, 4), 12)
        self.assertEqual(calc.multiplicar(2, 6), 12)
        self.assertEqual(calc.multiplicar(0, 10), 0)
```
