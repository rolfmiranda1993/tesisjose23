# Generated by Django 4.1.4 on 2022-12-20 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('pymes', '0004_departamento_rubro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubro',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.departamentod'),
        ),
    ]
