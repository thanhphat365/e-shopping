from django.shortcuts import render
from django.http import HttpResponse\

# Create your views here.
def store(request):
    return render(request, 'store.html')