# Generated by Django 3.2.5 on 2021-08-04 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_rename_author_blogpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, height_field=35, upload_to=None, width_field=45),
            preserve_default=False,
        ),
    ]
