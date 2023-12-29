# Generated by Django 5.0 on 2023-12-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tareas', '0014_tarea_observaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='observaciones',
        ),
        migrations.AddField(
            model_name='tarea',
            name='observaciones',
            field=models.ManyToManyField(blank=True, to='app_tareas.observacion'),
        ),
    ]
