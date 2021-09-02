# Generated by Django 3.2.6 on 2021-08-12 22:38

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]