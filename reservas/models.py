from django.db import models
from django.db import models

class Reserva(models.Model):
    fecha = models.DateField()
    nombre = models.CharField(max_length=100)
