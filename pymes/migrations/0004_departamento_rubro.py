# Generated by Django 4.1.4 on 2022-12-19 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pymes', '0003_alter_cliente_telefono_contacto_pagos'),
    ]

    operations = [
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de departamento')),
                ('jerarquia', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=20, verbose_name='Jerarquia asignada')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='rubro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymes.departamento')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
