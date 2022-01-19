from django.urls import path
from store import views

urlpatterns=[
    path("", views.store, name="store"),
    path("main/", views.main, name="main"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout")
]