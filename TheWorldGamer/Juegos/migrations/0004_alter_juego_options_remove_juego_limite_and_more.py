# Generated by Django 4.2 on 2023-04-27 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0003_juego_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='juego',
            options={'verbose_name': 'Juego', 'verbose_name_plural': 'Juegos'},
        ),
        migrations.RemoveField(
            model_name='juego',
            name='Limite',
        ),
        migrations.DeleteModel(
            name='Limite_alquiler',
        ),
    ]
