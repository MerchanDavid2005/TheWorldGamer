# Generated by Django 4.1.7 on 2023-05-04 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_pedido', models.CharField(max_length=50)),
                ('Imagen_pedido', models.ImageField(blank=True, null=True, upload_to='pedidos')),
                ('Numero_pedido', models.IntegerField()),
                ('Creacion_pedido', models.DateTimeField(auto_now_add=True)),
                ('Actualizacion_pedido', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
