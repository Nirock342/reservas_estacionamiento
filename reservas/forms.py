from django import forms
from tempus_dominus.widgets import DatePicker
from .models import Reserva


class ReservaForm(forms.ModelForm):
    fecha_reservada = forms.DateTimeField(
        widget=DatePicker(
            options={
                'format': 'YYYY-MM-DD',
                'useCurrent': True,
                'Collapse': False,
            }
        ),
        input_formats=[
            '%Y-%m-%d',       # Formato YYYY-MM-DD
            '%d/%m/%Y',       # Formato DD/MM/YYYY
            '%m/%d/%Y',       # Formato MM/DD/YYYY
            '%Y/%m/%d',       # Formato YYYY/MM/DD
        ]
    )
    
    class Meta:
        model = Reserva
        fields = ('fecha_reservada', 'hora_reservada', 'nombre', 'cedula', 'placa_vehiculo')
