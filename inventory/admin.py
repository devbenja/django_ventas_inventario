from django.contrib import admin
from .models import Category, Product, Client, Sale, DetSale

admin.site.register(Category) 
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Sale)
admin.site.register(DetSale)

