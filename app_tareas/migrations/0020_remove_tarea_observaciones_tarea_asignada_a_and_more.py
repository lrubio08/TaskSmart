# Generated by Django 5.0 on 2023-12-19 01:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tareas', '0019_remove_tarea_asignada_a'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='observaciones',
        ),
        migrations.AddField(
            model_name='tarea',
            name='asignada_a',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tareas_asignadas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Observacion',
        ),
    ]
