from rest_framework import generics
from .models import Paciente, Exame
from .serializers import PacienteSerializer, ExameSerializer


class PacienteList(generics.ListCreateAPIView):

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class ExameList(generics.ListCreateAPIView):

    queryset = Exame.objects.exclude(paciente__isnull=True)
    serializer_class = ExameSerializer

