# Generated by Django 2.1.5 on 2019-01-31 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190131_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='previoseorders',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='previoseorders',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]