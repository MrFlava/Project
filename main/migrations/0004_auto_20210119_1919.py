# Generated by Django 3.1.5 on 2021-01-19 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210119_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commented_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 19, 19, 35, 320625)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 19, 19, 35, 319999)),
        ),
    ]
