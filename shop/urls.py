from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("productview/<int:myid>",views.productview,name="Product"),
    path("checkout/",views.checkout,name="Checkout"),
    path("payment/",views.payment,name="payment")
    
    


]
