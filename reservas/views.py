from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReservaForm
from .models import Reserva

def reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('reservas:reserva_exitosa'))
    else:
        form = ReservaForm()
    
    context = {
        'form': form
    }
    return render(request, 'reservas/reserva.html', context)

def reserva_exitosa(request):
    return render(request, 'reservas/reserva_exitosa.html')
