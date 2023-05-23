from django.urls import path
from reservas import views
from .views import reserva, reserva_exitosa
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reservas'

urlpatterns = [
    path('reserva/', reserva, name='reserva'),
    path('reserva_exitosa/', views.reserva_exitosa, name='reserva_exitosa'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
