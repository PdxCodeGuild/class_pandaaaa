# Generated by Django 3.2.5 on 2021-07-29 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('H', 'HIGH'), ('M', 'MEDIUM'), ('L', 'LOW')], default='HIGH', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('completed_date', models.DateTimeField()),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.priority')),
            ],
        ),
    ]