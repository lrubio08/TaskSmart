from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada')
    )
    
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    asignada_a = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tareas_asignadas')
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, blank=True, null=True, related_name='tareas_con_prioridad')
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo

class Observacion(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
