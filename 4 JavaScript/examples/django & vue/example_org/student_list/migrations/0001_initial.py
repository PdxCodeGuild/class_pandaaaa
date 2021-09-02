# Generated by Django 3.2.6 on 2021-09-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cohort', models.CharField(max_length=50)),
                ('favorite_teacher', models.CharField(max_length=50)),
                ('captsone', models.URLField()),
            ],
        ),
    ]
