# Generated by Django 5.0 on 2023-12-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tareas', '0013_remove_tarea_observaciones_delete_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
    ]
