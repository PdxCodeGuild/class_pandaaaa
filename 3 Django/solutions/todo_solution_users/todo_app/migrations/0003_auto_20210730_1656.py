# Generated by Django 3.2.5 on 2021-07-30 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20191217_0523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('high', 'HIGH'), ('low', 'LOW'), ('medium', 'MEDIUM')], default='low', max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_app.priority'),
        ),
    ]