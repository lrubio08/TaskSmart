from django.apps import AppConfig
from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError


class AppTareasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_tareas'

    def ready(self):
        try:
            from django.contrib.sites.models import Site
            domain = 'tasksmart.luisrubiodev.tech' if not settings.DEBUG else '127.0.0.1:8000'
            
            Site.objects.update_or_create(
                id=1,
                defaults={
                    'domain': domain,
                    'name': 'TaskSmart'
                }
            )
        except (OperationalError, ProgrammingError):
            pass
