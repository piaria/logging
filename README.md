# Descripcion

Este proyecto muestra maneras de agregar atributos al logger en Django y lo hace por medio de agregar un middleware que procesa el request recopilando ciertos atributos y guardandolos en `threading.local()` para poder luego usarlos en el filtro (`RequestLogFilter`).

# Levantar el proyecto

- Para levantar el proyecto primero crear una carpeta donde se van a descargar los fuentes. 
- Clonar el repositorio con `git clone git@github.com:piaria/logging.git .`
- Luego crear el entorno virtual para ejecutarlo: `python3.10 -m venv .venv` y activarlo corriendo el comando `source .venv/bin/activate`
- Importar las dependencias ejecutando `pip install -r requirements.txt`
- Crear el esquema inicial de la base de datos con  `./manage.py migrate`
- Levantar el server `./manage.py runserver 0.0.0.0:8000`

Si todo salió bien se deberia obtener:
```bash
Performing system checks...

System check identified no issues (0 silenced).
October 07, 2022 - 21:28:37
Django version 4.1.2, using settings 'mysite.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

# Probar los logs

Para probar los logs se debe invocar el endpoint
```bash
http http://127.0.0.1:8000/tasks X-UOW:12345 -v
```

Se deberia mostrar en la consola del server algo como:
```
[2022-10-07 21:43:11,484] [server-host-name] [Anonymous] [12345] [7098347b-9ea9-420f-9e6d-49c5e7c25f10] [INFO] [views:12] in get tasks...
```