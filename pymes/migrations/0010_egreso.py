# Generated by Django 4.1.4 on 2022-12-21 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_cliented'),
        ('pymes', '0009_alter_ingreso_forma_de_pago_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='egreso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('forma_de_pago', models.CharField(max_length=200, verbose_name='Forma de Pago')),
                ('tipo_de_pago', models.CharField(max_length=200, verbose_name='Tipo de Pago')),
                ('nombre_de_pago', models.CharField(max_length=200, verbose_name='Nombre de Pago')),
                ('monto_de_pago', models.IntegerField(verbose_name='Monto de Pago')),
                ('numero_de_factura', models.CharField(max_length=200, verbose_name='Factura Nro')),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.rubrod')),
                ('titular_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.cliented')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
