from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Vista para la página de inicio del médico
def inicio_medico(request):
    return render(request, 'centro_medico/inicio_medico.html')

# Vista para la página de mis citas del médico
def mis_citas_medico(request):
    # Simulando una lista de citas; en un caso real, esto vendría de la base de datos
    citas = [{'id': 1, 'fecha': '2023-12-10', 'hora': '10:00', 'paciente': 'Juan Pérez'}]
    return render(request, 'centro_medico/mis_citas_medico.html', {'citas': citas})

# Vista para la página de cancelar citas del médico
def cancelar_cita_medico(request, cita_id):
    # Aquí iría la lógica para buscar y cancelar la cita con el ID proporcionado
    return render(request, 'centro_medico/cancelar_cita_medico.html')

# Vista para la página de cambiar cita del médico
def cambiar_cita_medico(request, cita_id):
    # Aquí iría la lógica para buscar y modificar la cita con el ID proporcionado
    return render(request, 'centro_medico/cambiar_cita_medico.html')

# Vista para la página de perfil del médico
def perfil_medico(request):
    # Simulando datos del perfil; en un caso real, esto vendría de la base de datos
    perfil = {'nombre': 'Dra. Ana Martínez', 'especialidad': 'Cardiología'}
    return render(request, 'centro_medico/perfil_medico.html', {'perfil': perfil})
