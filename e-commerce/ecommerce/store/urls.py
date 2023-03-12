from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
]