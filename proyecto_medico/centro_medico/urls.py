from django.urls import path
from . import views
from .views import cancelar_cita_medico, vista_general_cancelaciones
from django.contrib.auth.views import LogoutView
from .views import inicio
from .views import login_view
from .views import register
from .views import inicio_paciente

urlpatterns = [
    path('inicio-medico/', views.inicio_medico, name='inicio_medico'),
    path('mis-citas-medico/', views.mis_citas_medico, name='mis_citas_medico'),
    path('cancelar-cita/', vista_general_cancelaciones, name='vista_general_cancelaciones'),
    path('cancelar-cita-medico/<int:cita_id>/', cancelar_cita_medico, name='nombre_url_cancelar_cita'),
    path('cambiar-cita-medico/', views.cambiar_cita_medico, name='cambiar_cita_medico'),
    path('perfil-medico/', views.perfil_medico, name='perfil_medico'),
    path('cerrar-sesion/', LogoutView.as_view(next_page='nombre_url_inicio'), name='nombre_vista_cerrar_sesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('inicio-paciente/', inicio_paciente, name='inicio_paciente'),



]