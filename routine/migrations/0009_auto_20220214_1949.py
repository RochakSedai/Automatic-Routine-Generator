# Generated by Django 3.1.3 on 2022-02-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0008_auto_20220214_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_fourth',
            name='Lecturer_Name',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='computer_fourth',
            name='Lecturer_Subject',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]
