# Generated by Django 2.1.3 on 2018-11-27 04:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181127_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 27, 4, 4, 55, 28857, tzinfo=utc)),
        ),
    ]