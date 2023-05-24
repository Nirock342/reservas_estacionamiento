from django.db import models
from django.db import models

class Reserva(models.Model):
    fecha_reservada = models.DateField()
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, default='')
    placa_vehiculo = models.CharField(max_length=20, default='')
    hora_entrada = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre