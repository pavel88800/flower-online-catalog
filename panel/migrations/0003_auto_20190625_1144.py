# Generated by Django 2.2.1 on 2019-06-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_auto_20190625_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
