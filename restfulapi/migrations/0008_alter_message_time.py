# Generated by Django 4.0 on 2022-01-09 05:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restfulapi', '0007_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 9, 5, 28, 54, 661931, tzinfo=utc)),
        ),
    ]
