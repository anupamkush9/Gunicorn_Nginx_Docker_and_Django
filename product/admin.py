from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'updated_at', 'description']

admin.site.register(Product, ProductAdmin)