# Generated by Django 4.1.7 on 2023-04-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0002_limite_alquiler_dias_meses'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='juegos'),
        ),
    ]
