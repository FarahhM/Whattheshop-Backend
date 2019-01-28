# Generated by Django 2.1.5 on 2019-01-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_item_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('s', 'S'), ('l', 'L'), ('x', 'L')], default='x', max_length=5),
        ),
    ]
