# Generated by Django 4.0.3 on 2022-04-17 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionPedidos', '0002_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La dirección'),
        ),
    ]
