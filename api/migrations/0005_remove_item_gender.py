# Generated by Django 2.1.5 on 2019-01-25 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_preorders_userchoose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='gender',
        ),
    ]
