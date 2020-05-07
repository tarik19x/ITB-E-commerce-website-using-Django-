from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
import math
import json


# Create your views here.

def index(request):
    allproducts = []
    catprods = Product.objects.values('category', 'id')
    # databaser er sob gula row er id+ category chole asbe bt oikhabe obossi kichu onek dupliacate value thakbe oigula bad niye just unique category k seter maddhome bachai kora
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        # print("###--->",prod)
        n = len(prod)
        no_of_slide = n//4 + math.ceil(n/4-n//4)

        allproducts.append([prod, range(1, no_of_slide), no_of_slide])

    product_group = {'allproducts': allproducts}

    return render(request, "shop/index.html", product_group)


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.description.lower() or query in item.Product_name.lower() or query in item.category.lower():
        return True
    else:
        return False
def search(request):
    query = request.GET.get('search')
    allproducts = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        no_of_slide = n//4 + math.ceil(n/4-n//4)
        if len(prod) != 0:
            allproducts.append([prod, range(1, no_of_slide), no_of_slide])
    product_group = {'allproducts': allproducts,"msg":""}
    
    if len(allproducts) == 0 or len(query)<3:
        product_group={"msg":"please tell us more so that,we can find your product"}
        
    
    return render(request, 'shop/search.html', product_group)




def about(request):
    return render(request, "shop/about.html")


def contact(request):

    name = ""
    phone = ""
    email = ""
    desc = ""
    Thanks=""
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        # print("------>>",name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        Thanks = True
        return render(request, "shop/contact.html", {'Thanks': Thanks})
    return render(request, "shop/contact.html", {'Thanks': Thanks})



def productview(request, myid):

    product = Product.objects.filter(id=myid)
    # print("@@@@@@@",product)

    return render(request, "shop/prodView.html", {'product': product[0]})


def checkout(request):

    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        ammount = request.POST.get('ammount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email,
                       address=address, city=city, state=state, zip_code=zip_code, phone=phone,ammount=ammount)

        checklist = [items_json, name, email,
                     address, city, state, zip_code, phone]

        cnt = True

        for i in checklist:
            if not i:
                cnt = False
        id = 0
        if cnt:
            order.save()
            update = OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
            update.save()
            id = order.order_id

        return render(request, 'shop/checkout.html', {'id': id, 'checklist': checklist, 'cnt': cnt})
    return render(request, 'shop/checkout.html')


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')


def payment(request):
    return render(request, 'shop/payment.html')
    
