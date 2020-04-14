from django.db import models

# Create your models here.

class Product(models.Model):
    Product_id=models.AutoField
    Product_name=models.CharField(max_length=100)
    price= models.DecimalField(max_digits=12, decimal_places=0)
    desc=models.CharField(max_length=300)
    publish_date=models.DateField()