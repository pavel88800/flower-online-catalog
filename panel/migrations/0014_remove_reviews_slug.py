# Generated by Django 2.2.1 on 2019-07-08 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0013_auto_20190701_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='slug',
        ),
    ]
