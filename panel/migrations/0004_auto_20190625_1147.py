# Generated by Django 2.2.1 on 2019-06-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20190625_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
