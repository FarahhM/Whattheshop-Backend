# Generated by Django 2.1.5 on 2019-02-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20190131_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previoseorders',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
