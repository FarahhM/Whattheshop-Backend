# Generated by Django 2.1.5 on 2019-01-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190127_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('Men', 'MEN'), ('Women', 'WOMEN'), ('Kids', 'KIDS')], default='---', max_length=5),
        ),
    ]
