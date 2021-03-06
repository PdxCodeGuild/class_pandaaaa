# Generated by Django 3.2.5 on 2021-08-13 22:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chirp_app', '0003_auto_20210813_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postdate',
            field=models.DateField(default=datetime.datetime(2021, 8, 13, 22, 22, 6, 486181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posttime',
            field=models.TimeField(default=datetime.datetime(2021, 8, 13, 22, 22, 6, 486181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='joindate',
            field=models.DateField(default=datetime.datetime(2021, 8, 13, 22, 22, 6, 487178, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.ImageField(default=None, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateField(default=datetime.datetime(2021, 8, 13, 22, 22, 6, 490170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='posttime',
            field=models.TimeField(default=datetime.datetime(2021, 8, 13, 22, 22, 6, 490170, tzinfo=utc)),
        ),
    ]
