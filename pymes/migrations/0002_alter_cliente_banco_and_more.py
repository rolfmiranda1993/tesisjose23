# Generated by Django 4.1.4 on 2022-12-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='banco',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='documento_de_cuenta',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='forma_de_pago_habitual',
            field=models.CharField(blank=True, choices=[('1', 'Efectivo'), ('2', 'Cheque'), ('3', 'Transferencia'), ('4', 'Deposito')], max_length=20, null=True, verbose_name='Pago Habitual'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='mail_contacto_pagos',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Mail Conacto Pago'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='mail_del_nexo',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Mail Nexo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_contacto_pagos',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Contacto de pago'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_del_nexo',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nexo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='notas_adicionales',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Notas'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero_de_cuenta',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nro de Cuenta'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_del_nexo',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Tel. Nexo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_de_cuenta',
            field=models.CharField(blank=True, choices=[('Corriente', 'Corriente'), ('Ahorro', 'Ahorro'), ('Chequera', 'Chequera'), ('Nomina', 'Nomina'), ('Dolares', 'Dolares')], max_length=250, null=True, verbose_name='Tipo de Cuenta'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='titular_de_la_cuenta',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Titular de la cuenta'),
        ),
    ]