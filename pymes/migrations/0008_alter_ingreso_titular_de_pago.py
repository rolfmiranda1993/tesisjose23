# Generated by Django 4.1.4 on 2022-12-20 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_cliented'),
        ('pymes', '0007_alter_ingreso_rubro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso',
            name='titular_de_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.cliented'),
        ),
    ]