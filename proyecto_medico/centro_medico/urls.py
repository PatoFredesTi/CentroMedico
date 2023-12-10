from django.urls import path
from . import views

urlpatterns = [
    path('inicio-medico/', views.inicio_medico, name='inicio_medico'),
    path('mis-citas-medico/', views.mis_citas_medico, name='mis_citas_medico'),
    #path('cancelar-cita-medico/', views.cancelar_cita_medico, name='cancelar_cita_medico'),
    #path('cambiar-cita-medico/', views.cambiar_cita_medico, name='cambiar_cita_medico'),
    #path('perfil-medico/', views.perfil_medico, name='perfil_medico')
]