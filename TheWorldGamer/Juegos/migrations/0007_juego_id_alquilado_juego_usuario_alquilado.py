# Generated by Django 4.1.7 on 2023-05-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0006_remove_seccion_juego_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='Id_alquilado',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='juego',
            name='Usuario_alquilado',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
