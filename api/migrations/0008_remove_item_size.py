# Generated by Django 2.1.5 on 2019-01-27 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_item_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
    ]
