# Generated by Django 3.2.5 on 2021-07-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0011_alter_priority_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='choice',
            field=models.CharField(blank=True, choices=[('medium', 'MEDIUM'), ('low', 'LOW'), ('high', 'HIGH')], default='HIGH', max_length=7),
        ),
    ]