
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="About us"),
    path("contact",views.contact,name="Contact US"),
    path("tracker",views.tracker,name="TrackingStatus"),
    path("search",views.search,name="Search"),
    path("products/<int:myid>", views.prodview, name="Prodview"),
    path("checkout",views.checkout,name="Checkout"),
]