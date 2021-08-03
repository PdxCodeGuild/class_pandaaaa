# Generated by Django 3.2.5 on 2021-08-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0014_auto_20210730_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='choice',
            field=models.CharField(blank=True, choices=[('high', 'HIGH'), ('medium', 'MEDIUM'), ('low', 'LOW')], default='HIGH', max_length=7),
        ),
    ]