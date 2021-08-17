# Generated by Django 3.2.5 on 2021-08-13 22:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chirp_app', '0002_auto_20210813_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postdate',
            field=models.DateField(default=datetime.datetime(2021, 8, 13, 22, 19, 44, 996223, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posttime',
            field=models.TimeField(default=datetime.datetime(2021, 8, 13, 22, 19, 44, 996223, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='joindate',
            field=models.DateField(default=datetime.datetime(2021, 8, 13, 22, 19, 44, 996223, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.ImageField(default=None, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateField(default=datetime.datetime(2021, 8, 13, 22, 19, 45, 212, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='posttime',
            field=models.TimeField(default=datetime.datetime(2021, 8, 13, 22, 19, 44, 999215, tzinfo=utc)),
        ),
    ]