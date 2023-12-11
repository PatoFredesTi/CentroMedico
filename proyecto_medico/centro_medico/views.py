from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import PacienteRegisterForm
from django.contrib.auth import login
# Create your views here.
from django.shortcuts import render
from datetime import datetime, timedelta
from django.shortcuts import render

# Vista para la página de inicio del médico
def inicio_medico(request):
    return render(request, 'centro_medico/inicio_medico.html')

# Vista para la página de mis citas del médico
def mis_citas_medico(request):
    citas = [
        {'nombre_paciente': 'Juan Pérez', 'fecha': '2023-12-12', 'hora': '10:00', 'prevision': 'Fonasa'},
        {'nombre_paciente': 'Ana Soto', 'fecha': '2023-12-12', 'hora': '11:00', 'prevision': 'Isapre'},
        {'nombre_paciente': 'Mario Ruiz', 'fecha': '2023-12-12', 'hora': '12:00', 'prevision': 'Particular'},
        # ... más citas
    ]
    return render(request, 'centro_medico/mis_citas_medico.html', {'citas': citas})

# Vista para la página de cancelar citas del médico
def cancelar_cita_medico(request, cita_id):
    citas = [
        {'id': 1, 'nombre_paciente': 'Juan Pérez', 'fecha': '2023-12-12', 'hora': '10:00'},
        {'id': 2, 'nombre_paciente': 'Ana Soto', 'fecha': '2023-12-12', 'hora': '11:00'},
        {'id': 3, 'nombre_paciente': 'Mario Ruiz', 'fecha': '2023-12-12', 'hora': '12:00'}
        # ... más citas
    ]
    return render(request, 'centro_medico/cancelar_cita_medico.html', {'citas': citas})

def vista_general_cancelaciones(request):
    # Simula obtener todas las citas de alguna manera
    citas = [
        {'nombre_paciente': 'Juan Pérez', 'fecha': '2023-12-12', 'hora': '10:00'},
        {'nombre_paciente': 'Ana Soto', 'fecha': '2023-12-12', 'hora': '11:00'},
        {'nombre_paciente': 'Mario Ruiz', 'fecha': '2023-12-12', 'hora': '12:00'}
    ]
    return render(request, 'centro_medico/vista_general_cancelaciones.html', {'citas': citas})

# Vista para la página de cambiar cita del médico
def cambiar_cita_medico(request):
    citas = [
        {'id': 1, 'nombre_paciente': 'Juan Pérez', 'fecha': '2023-12-12', 'hora': '10:00'},
        {'id': 2, 'nombre_paciente': 'Ana Soto', 'fecha': '2023-12-12', 'hora': '11:00'},
        # ... más citas
    ]
    return render(request, 'centro_medico/cambiar_cita_medico.html', {'citas': citas})

# Vista para la página de perfil del médico
# centro_medico/views.py

def perfil_medico(request):
    perfil = {
        'nombre': 'Dr. Juan Pérez',
        'correo': 'juan.perez@centromedico.com',
        'especialidad': 'Cardiología',
        'foto_perfil': 'url_de_la_imagen.jpg'  # Asegúrate de tener esta imagen en tus archivos estáticos
    }
    return render(request, 'centro_medico/perfil_medico.html', {'perfil': perfil})

def inicio(request):
    testimonios = [
        {'autor': 'Ana López', 'texto': 'Excelente atención y profesionalismo.'},
        {'autor': 'Carlos Hernández', 'texto': 'Muy satisfecho con el servicio recibido.'},
        {'autor': 'Laura Martínez', 'texto': 'Personal amable y muy preparado.'},
        {'autor': 'Pedro Álvarez', 'texto': 'Instalaciones cómodas y limpias.'},
        {'autor': 'Sofía Gómez', 'texto': 'Recomendado para toda la familia.'},
    ]
    return render(request, 'centro_medico/inicio.html', {'testimonios': testimonios})

def contacto(request):
    # Aquí podrías añadir lógica para manejar la información del formulario si es necesario
    return render(request, 'centro_medico/contacto.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirige en función del tipo de usuario seleccionado
            tipo_usuario = request.POST.get('tipo_usuario', 'medico')
            if tipo_usuario == 'medico':
                return redirect('nombre_url_vista_medico')  # Cambiar a la URL de la vista del médico
            else:
                return redirect('nombre_url_vista_paciente')  # Cambiar a la URL de la vista del paciente
        else:
            # Manejar el caso de login fallido
            pass

    return render(request, 'centro_medico/login.html')

def register(request):
    if request.method == 'POST':
        form = PacienteRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('nombre_url_vista_paciente_post_registro')
    else:
        form = PacienteRegisterForm()
    return render(request, 'centro_medico/register.html', {'form': form})

def inicio_paciente(request):
    # Simulación de datos de citas
    fecha_actual = datetime.now()
    citas = [
        {'fecha': fecha_actual + timedelta(days=1), 'hora': '10:00', 'especialista': 'Dr. García'},
        {'fecha': fecha_actual + timedelta(days=3), 'hora': '11:30', 'especialista': 'Dra. Martínez'}
    ]
    
    tiene_citas = len(citas) > 0
    return render(request, 'centro_medico/inicio_paciente.html', {'citas': citas, 'tiene_citas': tiene_citas})


def mis_citas_paciente(request):
    # Código para obtener datos de las citas, si es necesario
    return render(request, 'centro_medico/mis_citas_paciente.html')