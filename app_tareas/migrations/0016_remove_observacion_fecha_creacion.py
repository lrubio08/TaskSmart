# Generated by Django 5.0 on 2023-12-18 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tareas', '0015_observacion_remove_tarea_observaciones_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observacion',
            name='fecha_creacion',
        ),
    ]
