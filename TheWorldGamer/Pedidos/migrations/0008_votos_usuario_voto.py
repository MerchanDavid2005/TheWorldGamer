# Generated by Django 4.2 on 2023-05-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0007_votos'),
    ]

    operations = [
        migrations.AddField(
            model_name='votos',
            name='Usuario_voto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
