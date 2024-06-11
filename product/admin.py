from django.contrib import admin
from .models import Product, Document

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'updated_at', 'description']

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_file']

admin.site.register(Product, ProductAdmin)
admin.site.register(Document, DocumentAdmin)