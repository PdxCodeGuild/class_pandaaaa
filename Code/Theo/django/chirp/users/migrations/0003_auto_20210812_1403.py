# Generated by Django 3.2.6 on 2021-08-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]