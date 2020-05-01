from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math


# Create your views here.

def index(request):
    # product_list=Product.objects.all()
    # print(len(product_list))
    
    allproducts=[]
    
    catprods=Product.objects.values('category','id')
    # databaser er sob gula row er id+ category chole asbe bt oikhabe obossi kichu onek dupliacate value thakbe oigula bad niye just unique category k seter maddhome bachai kora
    cats={item['category'] for item in catprods }
    # print("catprods----->",catprods)
    # print("cats---->>",cats)
    
    
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        # print("###--->",prod)
        n=len(prod)
        no_of_slide=n//4 +math.ceil(n/4-n//4)
        
        allproducts.append([prod,range(1,no_of_slide),no_of_slide])
        
        
        
        
        
    
    # print("catprods----->",catprods)
    # print("cat---->>",cats)
     



    # allproducts=[[product_list,range(1,no_of_slide),no_of_slide],[product_list,range(1,no_of_slide),no_of_slide]]
    product_group={'allproducts':allproducts}

    return render(request,"shop/index.html",product_group)


def about(request):
    return render(request,"shop/about.html")    

def contact(request):
    return render(request,"shop/index.html")


def search(request):
    return render(request,"shop/index.html")


def productview(request):
    return render(request,"shop/index.html")

def checkout(request):
    return render(request,"shop/index.html")

def tracker(request):
    return render(request,"shop/index.html")