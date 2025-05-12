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

## ⚙️ Jenkinsfile

Se define una pipeline de Jenkins que clona el repositorio y ejecuta los tests unitarios con `unittest`.

### Ejemplo de pipeline (también presente en los assets):

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

## 📷 Capturas de la práctica

### ✅ Código funcional de la calculadora

![Código Python](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/1-Calculadora.PNG)

### ✅ Pruebas unitarias ejecutándose correctamente

![Unittest funcionando](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/2-UniTest.PNG)

### ✅ Jenkins en ejecución vía Docker

![Jenkins activo](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/6-JenkinsActivo.PNG)

### ✅ Docker Compose levantando Jenkins

![Jenkins con Docker](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/3-PuestaEnMarcha.PNG)

### ✅ Contraseña inicial obtenida del contenedor

![Contraseña inicial Jenkins](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/4-ContraseñaTemporal.PNG)

### ✅ Plugins recomendados en instalación

![Plugins Jenkins](https://github.com/marconajcoz/pps-1033563/raw/main/RA5/RA5_1/assets/Imagenes/5-InstalarPlugins.PNG)

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

---

## 🚣 Jenkins con Docker

Para levantar Jenkins de forma local:

```bash
docker-compose up -d
```

Esto lanza Jenkins en `http://localhost:8080`. La contraseña inicial se extrae con:

```bash
docker exec -it jenkins_jenkins_1 cat /var/jenkins_home/secrets/initialAdminPassword
```

---

## 📌 Pendiente en próximos pasos

* Crear y probar el `jenkinsfile.docker` (con stages Docker + Docker Compose)
* Añadir más pruebas o pasos de despliegue
