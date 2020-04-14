# Generated by Django 3.0.4 on 2020-04-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
