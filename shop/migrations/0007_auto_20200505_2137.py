# Generated by Django 3.0.4 on 2020-05-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_name',
            field=models.CharField(max_length=45),
        ),
    ]
