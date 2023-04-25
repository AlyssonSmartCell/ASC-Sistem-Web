from django.db import models
from datetime import datetime

class ordens_servico(models.Model):
    #dados cliente
    cliente = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    contato = models.FloatField()
    data = models.DateField(default=datetime.now)

    #dados celular
    modelo = models.TextField(max_length=10)
    marca = models.TextField(max_length=10)
    avarias = models.BooleanField(default=False)
    if avarias == True:
        tipo_avaria = models.TextField()
    else:
        pass

    #checkList

    bateria = models.BooleanField(default=False)
    cartao_memoria = models.BooleanField(default=False)
    chip = models.BooleanField(default=False)
    tampa = models.BooleanField(default=False)
    capa = models.BooleanField(default=False)
    tela = models.BooleanField(default=False)
    display = models.BooleanField(default=False)
    touch = models.BooleanField(default=False)
    ligando = models.BooleanField(default=False)
    vibrando = models.BooleanField(default=False)
    oxidacao = models.BooleanField(default=False)
    botao_home = models.BooleanField(default=False)
    botao_power = models.BooleanField(default=False)
    botoes_volume = models.BooleanField(default=False)
    conector_carga = models.BooleanField(default=False)
    slot_chip= models.BooleanField(default=False)
    outros = models.BooleanField(default=False)
    bateria = models.BooleanField(default=False)

    #senha

    senha = models.BooleanField(default=False)

    #valor
    valor = models.FloatField

    #defeito apontado pelo cliente
    defeito = models.TextField(max_length=50)




