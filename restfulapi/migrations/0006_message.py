# Generated by Django 4.0 on 2022-01-09 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('restfulapi', '0005_alter_captcha_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
