# Generated by Django 4.2 on 2023-05-08 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registros', '0003_registro_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='Usuario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
