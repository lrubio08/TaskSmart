# Generated by Django 4.2.4 on 2023-09-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tareas', '0006_alter_tarea_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
    ]
