# Generated by Django 4.2.4 on 2023-09-06 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tareas', '0007_alter_tarea_observaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='observaciones',
        ),
        migrations.CreateModel(
            name='Observaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observaciones_rel', to='app_tareas.tarea')),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='observaciones',
            field=models.ManyToManyField(related_name='tarea_rel', to='app_tareas.observaciones'),
        ),
    ]