# Generated by Django 3.2.5 on 2021-08-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletes', '0003_auto_20210810_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolete',
            name='name_in_naboletes',
            field=models.CharField(default='na', max_length=250),
            preserve_default=False,
        ),
    ]
