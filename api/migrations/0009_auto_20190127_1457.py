# Generated by Django 2.1.5 on 2019-01-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_item_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('Men', 'MEN'), ('Women', 'WOMEN'), ('Kids', 'KIDS')], default='', max_length=5),
        ),
    ]