# Generated by Django 4.2 on 2023-05-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0002_alter_pedido_imagen_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='Imagen_pedido',
            field=models.ImageField(blank=True, null=True, upload_to='pedidos'),
        ),
    ]
