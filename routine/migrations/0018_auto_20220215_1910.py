# Generated by Django 3.1.3 on 2022-02-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0017_auto_20220215_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_first',
            name='Lecturer_Period',
            field=models.IntegerField(default=0, null=True),
        ),
    ]