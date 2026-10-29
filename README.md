
# Tasksmart

Aplicación web de gestión de tareas desarrollada con **Django**, diseñada para ayudar a los usuarios a organizar, priorizar y dar seguimiento a sus pendientes de manera eficiente.

Demo: https://tasksmart.luisrubiodev.tech

La aplicación corre en Heroku utilizando PostgreSQL en producción y un diseño optimizado para una experiencia fluida.

## Caprturas
<img width="700"  alt="tasksmart" src="https://github.com/user-attachments/assets/ee1f6e2d-6dd8-4188-8381-1f47094d7a7d" />


## Cómo funciona

- **Autenticación de usuarios:** Sistema completo de registro, inicio de sesión y cierre de sesión seguro.
- **Gestión de Tareas:** Creación, edición, marcado como completado y eliminación de tareas personales.
- **Panel de Administración:** Gestión centralizada desde el admin de Django para supervisar usuarios y registros de la plataforma.
- **Interfaz Responsiva:** Diseño limpio adaptado para dispositivos móviles y de escritorio.


## Tecnologías

- Python 3.12 y Django
- HTML, CSS, JavaScript y Bootstrap
- PostgreSQL (en producción) / SQLite (en desarrollo)
- Gunicorn y WhiteNoise
- Despliegue en Heroku

## Estructura

```
tasksmart/
├── app_tareas/          # app principal: vistas, plantillas y lógica
├── tasksmart/
│   └── settings/
│       ├── base.py        # configuración común
│       ├── development.py # entorno local
│       └── production.py  # entorno de producción (Heroku)
├── static/
├── Procfile
├── requirements.txt
└── manage.py
```

## Ejecutar en local

```bash
git clone https://github.com/lrubio08/tasksmart.git
cd tasksmart
python -m venv venv
venv\Scripts\activate        # en macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## Crea un archivo `.env` en la raíz (no se sube a Git):

```
SECRET_KEY=tu-clave-secreta-de-django

# Credenciales de Zoho Mail
EMAIL_HOST_USER=tu-correo@tu-dominio.com
EMAIL_HOST_PASSWORD=tu-contraseña-de-aplicacion-de-zoho
```
## Configuraciones envió de correos 
```
# Configuración de Correo (puedes usar Zoho Mail u otro proveedor SMTP para el envío de correos):
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'TaskSmart <dominio@dominio.com>'
```


```bash
python manage.py migrate
python manage.py runserver
```

## Despliegue en Heroku

El `Procfile` aplica las migraciones y arranca Gunicorn:

```
web: python manage.py migrate --noinput && gunicorn moviplus.wsgi --log-file -
```

Variables de entorno que hay que cargar en Heroku: `DJANGO_SETTINGS_MODULE`, `SECRET_KEY`, `TMDB_API_KEY`, `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS`.

## Problemas que tuve que resolver

* Error 500 persistente en el panel de administración (/admin/) en producción.

* Causa: Se produjo un desfase en el modelo de sitios de Django (django.contrib.sites).
  La configuración del proyecto exigía estrictamente SITE_ID = 1,
  pero la base de datos PostgreSQL en producción había registrado el dominio con un ID distinto (id=2),
  lo que provocaba un fallo de tipo DoesNotExist al intentar renderizar la vista de inicio de sesión del administrador.

* Solución: Se accedió a la consola interactiva de Heroku (python manage.py shell),
  se eliminaron los registros desfasados de la tabla django_site y se recreó de forma limpia y
  explícita el registro asignándole de manera exacta el id=1 junto al dominio oficial de producción (tasksmart.luisrubiodev.tech).


## Autor

* Luis Rubio, desarrollador Full Stack Python.
* Portafolio: https://luisrubiodev.tech/
* GitHub: https://github.com/lrubio08
* LinkedIn: https://www.linkedin.com/in/luis-rubio-ram%C3%ADrez/
