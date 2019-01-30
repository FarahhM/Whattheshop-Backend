# Generated by Django 2.1.5 on 2019-01-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190129_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
        migrations.AddField(
            model_name='userchocie',
            name='size',
            field=models.CharField(default=0.0004970178926441351, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('---', '__'), ('Men', 'MEN'), ('Women', 'WOMEN'), ('Kids', 'KIDS')], default='---', max_length=33),
        ),
    ]