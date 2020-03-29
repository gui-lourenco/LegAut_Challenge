# Generated by Django 3.0.4 on 2020-03-28 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_search_last_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='marital_status',
            field=models.CharField(choices=[(1, 'Solteiro(a)'), (2, 'Casado(a)'), (3, 'Viúvo(a)'), (4, 'Divorciado(a)')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='sex',
            field=models.CharField(choices=[(1, 'Masculino'), (2, 'Feminino')], max_length=9, null=True),
        ),
    ]
