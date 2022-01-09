# Generated by Django 4.0 on 2022-01-09 05:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('restfulapi', '0009_alter_message_time_alter_message_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 9, 5, 34, 49, 959717, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
