# Generated by Django 4.2.1 on 2023-05-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0006_alter_reserva_cedula_alter_reserva_placa_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cedula',
            field=models.CharField(default='', max_length=20),
        ),
    ]
