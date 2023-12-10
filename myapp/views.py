from django.shortcuts import render
from django.http import HttpResponse\

# Create your views here.
def store(request):
    return render(request, 'store.html')
def cart (request):
    return render (request,"cart.html",{})
def check_out (request):
    return render (request,"check_out.html",{})