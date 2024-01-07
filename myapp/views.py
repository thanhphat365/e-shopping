from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartitems,Customer,Product,Cart
from django.http import JsonResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
import requests
# Create your views Cartitems)
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        global cart
        cart, created = Cart.objects.get_or_create(customer = customer,completed=False)
        cartitems = cart.cartitems_set.all()
    products = Product.objects.all()
    paginator = Paginator(products , 3)
    pageNumber = request.GET.get("page")
    try:
        products = paginator.page(pageNumber)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage :
        products =paginator.page(paginator.num_pages)
    return render(request, 'store.html',{"products":products,"cart":cart})
def cart (request):
    return render (request,"cart.html",{})
def check_out (request):
    return render (request,"check_out.html",{})