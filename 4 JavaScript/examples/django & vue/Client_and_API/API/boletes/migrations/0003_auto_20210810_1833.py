# Generated by Django 3.2.5 on 2021-08-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletes', '0002_rename_book_bolete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolete',
            name='chemical_tests',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='common_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='edibility',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='genus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='links',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='other_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='science_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='species',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bolete',
            name='tells',
            field=models.TextField(blank=True, null=True),
        ),
    ]
