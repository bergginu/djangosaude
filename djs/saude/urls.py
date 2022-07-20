from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pacientes/$', views.PacienteList.as_view(), name='paciente-list'),
    url(r'^exames/$', views.ExameList.as_view(), name='exame-list'),
]