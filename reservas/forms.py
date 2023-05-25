from django import forms
from tempus_dominus.widgets import DatePicker
from .models import Reserva
from django import forms



class ReservaForm(forms.ModelForm):
    fecha_reservada = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = Reserva
        fields = ('fecha_reservada', 'hora_reservada', 'nombre', 'cedula', 'placa_vehiculo')
