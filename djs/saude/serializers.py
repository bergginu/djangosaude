from rest_framework import serializers
from .models import Paciente
from .models import Exame

class PacienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Paciente
        fields = '__all__'


class ExameSerializer(serializers.ModelSerializer):

    class Meta:

        model = Exame
        fields = '__all__'