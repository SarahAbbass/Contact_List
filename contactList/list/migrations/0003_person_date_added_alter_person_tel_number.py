# Generated by Django 4.2.5 on 2023-09-25 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_alter_person_tel_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_added',
            field=models.DateField(default=datetime.date(2023, 9, 25)),
        ),
        migrations.AlterField(
            model_name='person',
            name='tel_number',
            field=models.CharField(max_length=20),
        ),
    ]
