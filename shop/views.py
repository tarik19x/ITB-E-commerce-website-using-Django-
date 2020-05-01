from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math


# Create your views here.

def index(request):
    product_list=Product.objects.all()
    # print(len(product_list))
    n=len(product_list)
    no_of_slide=n//4 +math.ceil(n/4-n//4)
    print(no_of_slide)

    allproducts=[[product_list,range(1,no_of_slide),no_of_slide],[product_list,range(1,no_of_slide),no_of_slide]]
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