# Generated by Django 2.1.5 on 2019-02-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190203_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='previoseorders',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]