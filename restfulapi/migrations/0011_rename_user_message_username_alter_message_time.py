# Generated by Django 4.0 on 2022-01-15 10:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restfulapi', '0010_alter_message_time_alter_message_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 15, 10, 46, 30, 724168, tzinfo=utc)),
        ),
    ]
