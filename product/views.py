from django.shortcuts import render
import socket
from django.http import HttpResponse, JsonResponse
from .models import Product
 
 
def index(request):
    host = socket.gethostname()
    context = {'products': Product.objects.all(), "host": host}

    return render(request,'product/checkout.html', context)

def get_drf_ip(request):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # return HttpResponse(f'hostname {hostname} ip_address {ip_address}')
    return JsonResponse({
        'hostname': hostname,
        'ip_address': ip_address,
    })