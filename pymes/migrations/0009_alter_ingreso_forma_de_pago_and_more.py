# Generated by Django 4.1.4 on 2022-12-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymes', '0008_alter_ingreso_titular_de_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso',
            name='forma_de_pago',
            field=models.CharField(blank=True, choices=[('1', 'Efectivo'), ('2', 'Cheque'), ('3', 'Transferencia'), ('4', 'Deposito')], max_length=200, null=True, verbose_name='Forma de Pago'),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='tipo_de_cobro',
            field=models.CharField(blank=True, choices=[('1', 'Efectivo'), ('2', 'Cheque'), ('3', 'Transferencia'), ('4', 'Deposito')], max_length=200, null=True, verbose_name='Tipo de cobro'),
        ),
    ]