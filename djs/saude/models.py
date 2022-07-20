from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=64)
    idade = models.PositiveSmallIntegerField()
    endereco = models.CharField(max_length=128)

    def __str__(self):
        return self.nome



class Exame(models.Model):
    nome_prof = models.CharField(max_length=64)
    dt_exame = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return self.nome