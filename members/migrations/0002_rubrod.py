# Generated by Django 4.1.4 on 2022-12-20 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rubroD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('staff_name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.departamentod')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
