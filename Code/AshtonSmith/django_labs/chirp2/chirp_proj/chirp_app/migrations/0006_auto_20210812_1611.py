# Generated by Django 3.2.5 on 2021-08-12 23:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chirp_app', '0005_auto_20210812_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='postdate',
            field=models.DateField(default=datetime.datetime(2021, 8, 12, 23, 11, 34, 676049, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posttime',
            field=models.TimeField(default=datetime.datetime(2021, 8, 12, 23, 11, 34, 676049, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='joindate',
            field=models.DateField(default=datetime.datetime(2021, 8, 12, 23, 11, 34, 677045, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateField(default=datetime.datetime(2021, 8, 12, 23, 11, 34, 679040, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='posttime',
            field=models.TimeField(default=datetime.datetime(2021, 8, 12, 23, 11, 34, 679040, tzinfo=utc)),
        ),
    ]
