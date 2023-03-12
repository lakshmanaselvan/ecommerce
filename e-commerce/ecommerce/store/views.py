from django.shortcuts import render
from .models import *
def store(request):
    products = product.objects.all()
    context = {'products':products}
    return render(request,'store.html',context)

def cart(request):
    return render(request,'cart.html',{})

def checkout(request):
    return render(request,'checkout.html',{})