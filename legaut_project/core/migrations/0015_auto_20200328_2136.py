# Generated by Django 3.0.4 on 2020-03-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200328_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='marital_status',
            field=models.IntegerField(choices=[(1, 'Solteiro(a)'), (2, 'Casado(a)'), (3, 'Viúvo(a)'), (4, 'Divorciado(a)')], null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino')], null=True),
        ),
    ]
