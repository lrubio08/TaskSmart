from django.apps import AppConfig
from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError


class AppTareasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_tareas'

    def ready(self):
        # Asegura que el Site esté configurado correctamente al iniciar
        try:
            from django.contrib.sites.models import Site
            domain = 'tasksmart.luisrubiodev.tech' if not settings.DEBUG else '127.0.0.1:8000'

            site, created = Site.objects.get_or_create(
                domain=domain,
                defaults={'name': 'TaskSmart'}
            )

            if not created and site.name != 'TaskSmart':
                site.name = 'TaskSmart'
                site.save()

        except (OperationalError, ProgrammingError):

            pass