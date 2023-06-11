from django.shortcuts import render
import socket
from django.http import HttpResponse
from .models import Product
 
 
def index(request):
    host = socket.gethostname()
    context = {'products': Product.objects.all(), "host": host}

    return render(request,'product/checkout.html', context)
