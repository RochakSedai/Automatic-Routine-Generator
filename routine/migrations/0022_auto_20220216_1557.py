# Generated by Django 3.1.3 on 2022-02-16 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0021_auto_20220216_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer_first',
            old_name='Lab_Period',
            new_name='Lab_Lec_Period',
        ),
    ]
