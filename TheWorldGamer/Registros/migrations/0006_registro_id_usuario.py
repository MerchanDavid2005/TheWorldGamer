# Generated by Django 4.1.7 on 2023-05-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registros', '0005_alter_registro_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='Id_usuario',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
