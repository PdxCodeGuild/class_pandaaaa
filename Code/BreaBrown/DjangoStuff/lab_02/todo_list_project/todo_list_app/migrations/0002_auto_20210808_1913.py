# Generated by Django 3.2.6 on 2021-08-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_text',
            new_name='task_title',
        ),
        migrations.AddField(
            model_name='task',
            name='task_detail',
            field=models.CharField(default='NONE', max_length=200),
            preserve_default=False,
        ),
    ]