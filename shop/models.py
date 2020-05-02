from django.db import models

# Create your models here.

class Product(models.Model):
    Product_id=models.AutoField
    Product_name = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=12, decimal_places=0)
    desc=models.CharField(max_length=300)
    publish_date=models.DateField()
    category= models.CharField( max_length=50,default="")
    subcategory = models.CharField( max_length=50,default="")
    image = models.ImageField(upload_to="shop/images",default="")
   
    def __str__(self):
        return self.Product_name
    
    

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
