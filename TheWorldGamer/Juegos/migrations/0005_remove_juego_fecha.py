# Generated by Django 4.1.7 on 2023-05-03 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0004_alter_juego_options_remove_juego_limite_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='Fecha',
        ),
    ]
