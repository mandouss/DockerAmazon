# Generated by Django 2.0 on 2018-04-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20180427_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=119, unique=True),
        ),
    ]
