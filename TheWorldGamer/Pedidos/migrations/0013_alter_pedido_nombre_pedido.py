# Generated by Django 4.1.7 on 2023-05-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0012_pedido_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='Nombre_pedido',
            field=models.CharField(max_length=100),
        ),
    ]