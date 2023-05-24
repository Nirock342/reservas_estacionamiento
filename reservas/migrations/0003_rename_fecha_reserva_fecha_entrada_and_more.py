# Generated by Django 4.2.1 on 2023-05-24 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reserva_cedula_reserva_hora_entrada_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='fecha',
            new_name='fecha_entrada',
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_solicitud',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cedula',
            field=models.CharField(default='CC', max_length=10),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_entrada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='placa_vehiculo',
            field=models.CharField(default='Ingrese Placa', max_length=20),
        ),
    ]