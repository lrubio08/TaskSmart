from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Etiqueta, Tarea, Prioridad
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import ssl
import smtplib
from django.conf import settings
from email.mime.multipart import MIMEMultipart
from .forms import ObservacionForm, RegistroForm, TareaForm, FiltroTareasForm
from email.mime.text import MIMEText

# Create your views here.
def index (request):
    return render (request, 'app_tareas/index.html')


def registro(request):
    try:
        if request.method == 'POST':
            print(f"Datos POST recibidos: {request.POST}")
            form = RegistroForm(request.POST)
            if form.is_valid():
                user = form.save()
                print(user)
                messages.success(request, 'Te has registrado exitosamente. Ahora puedes iniciar sesión.')
                return redirect('iniciar_sesion')
        else:
            form = RegistroForm()
        return render(request, 'app_tareas/registro.html', {'form': form})
    except Exception as e:
        print(f"Error en la vista de registro: {e}")
        raise

def registro_exitoso(request):
    return render(request, 'app_tareas/registro_exitoso.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El inicio de sesión es exitoso, redirigir a la vista sesion_iniciada
            login(request, user)
        else:
            messages.error(request, '¡Nombre de usuario o contraseña incorrectos!')
            return render(request, 'app_tareas/login.html')
        return redirect('listar_tareas')
    return render(request, 'app_tareas/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

@login_required
def listar_tareas(request):
    form = FiltroTareasForm(request.GET)
    tareas_pendientes = Tarea.objects.filter(usuario=request.user, estado='pendiente').order_by('fecha_vencimiento')
    if form.is_valid() and form.cleaned_data['etiqueta']:
        tareas_pendientes = tareas_pendientes.filter(etiqueta=form.cleaned_data['etiqueta'])
    return render (request, 'app_tareas/listar_tareas.html', {'tareas_pendientes':tareas_pendientes, 'form': form,  })

@login_required
def ver_tarea(request):
    user = request.user
    tareas = Tarea.objects.filter(Q(asignada_a=user) | Q(usuario=user))
    prioridad = tareas.prioridad if hasattr(tareas, 'prioridad') else None
    form_observacion = ObservacionForm()
    return render(request, 'app_tareas/ver_tarea.html', {'tareas': tareas, 'prioridad': prioridad, 'form_observacion': form_observacion, })

@login_required
def crear_tarea(request):
    prioridades = Prioridad.objects.all()
    if request.method == 'POST':
        form = TareaForm(request.POST) 
        if form.is_valid():
            tarea = form.save(commit=False)

            tarea.usuario =request.user
            asignada_a = form.cleaned_data.get('asignada_a')
            tarea.asignada_a = asignada_a
            form.save()
            return redirect('listar_tareas')
    else:
        form = TareaForm()
    return render(request,'app_tareas/formulario_tarea.html', {'form':form, 'titulo': 'Crear Tarea', 'boton': 'Guardar Tarea','editando':False, 'prioridades':prioridades})
@login_required
def eliminar_tarea(request, tarea_id):
        tarea = Tarea.objects.get(pk=tarea_id)
        tarea.delete()
        return redirect('ver_tarea')
    
@login_required
def completar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    tarea.estado = 'completada'
    tarea.save()
    return redirect('ver_tarea')

@login_required
def editar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('ver_tarea')
    else:
        form = TareaForm(instance=tarea)
        
    return render(request, 'app_tareas/formulario_tarea.html', {'form':form, 'titulo': 'Editar Tarea', 'boton': 'Guardar Cambios', 'tarea':tarea, 'editando':True})
@login_required
def crear_observacion(request, tarea_id):
    tarea = get_object_or_404(Tarea, id= tarea_id)
    if request.method == 'POST':
        form = ObservacionForm(request.POST)
        if form.is_valid():
            observacion = form.save(commit=False)
            observacion.tarea = tarea
            observacion.save()
            
            tarea.observaciones += f"{observacion.contenido}\n"
            tarea.save()
            return redirect('ver_tarea')
        else:
            form = ObservacionForm()
        return render(request, 'app_tareas/ver_tarea', {'form':form})
