# Generated by Django 4.1.7 on 2023-05-09 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0007_juego_id_alquilado_juego_usuario_alquilado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='Id_alquilado',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='Usuario_alquilado',
        ),
    ]
