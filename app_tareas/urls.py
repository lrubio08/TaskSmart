from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('listar_tareas/', views.listar_tareas, name = 'listar_tareas'),
    path('ver_tarea/', views.ver_tarea, name= 'ver_tarea'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('eliminar_tarea/<int:tarea_id>', views.eliminar_tarea, name='eliminar_tarea'),
    path('completar_tarea/<int:tarea_id>', views.completar_tarea, name='completar_tarea'),
    path('editar_tarea/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('crear_observacion/<int:tarea_id>/', views.crear_observacion, name='crear_observacion'),
]
