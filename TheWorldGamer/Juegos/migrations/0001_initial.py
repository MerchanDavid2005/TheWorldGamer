# Generated by Django 4.1.7 on 2023-04-26 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Limite_alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Limite', models.IntegerField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Limite',
                'verbose_name_plural': 'Limites',
            },
        ),
        migrations.CreateModel(
            name='Seccion_Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seccion', models.CharField(max_length=50)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Seccion',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.IntegerField()),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
                ('Limite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juegos.limite_alquiler')),
                ('Seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juegos.seccion_juego')),
            ],
        ),
    ]