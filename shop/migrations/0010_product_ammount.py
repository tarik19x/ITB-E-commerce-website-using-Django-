# Generated by Django 3.0.4 on 2020-05-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200506_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ammount',
            field=models.IntegerField(default=0),
        ),
    ]
