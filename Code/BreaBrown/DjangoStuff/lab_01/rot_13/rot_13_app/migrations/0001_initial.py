# Generated by Django 3.2.6 on 2021-08-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cypher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]
