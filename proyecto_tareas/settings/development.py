from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_PORT = 2525
EMAIL_USE_TLS = False  # 👈 cambia a False
EMAIL_USE_SSL = False  # 👈 agrega esto
EMAIL_HOST_USER = '015f921d6ce662'
EMAIL_HOST_PASSWORD = '50215f9c69c3a8'
DEFAULT_FROM_EMAIL = 'Luis Rubio Dev <luisdev@luisrubiodev.tech>'