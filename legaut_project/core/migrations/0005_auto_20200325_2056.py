# Generated by Django 3.0.4 on 2020-03-25 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200325_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='adress',
            new_name='address',
        ),
    ]
