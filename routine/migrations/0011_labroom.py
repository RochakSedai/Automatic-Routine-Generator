# Generated by Django 3.1.3 on 2022-02-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0010_auto_20220214_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lab_Name', models.CharField(max_length=50)),
                ('Lab_No', models.IntegerField()),
            ],
        ),
    ]