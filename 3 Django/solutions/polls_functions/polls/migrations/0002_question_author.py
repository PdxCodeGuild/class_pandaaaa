# Generated by Django 3.2.5 on 2021-07-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.CharField(default='sb', max_length=20),
            preserve_default=False,
        ),
    ]