from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Reserva

class ReservaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=DatePickerInput(format='%Y-%m-%d')
    )

    class Meta:
        model = Reserva
        fields = ('fecha', 'nombre')
