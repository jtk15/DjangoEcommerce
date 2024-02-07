from django.contrib import admin

from .models import Product, Category


class AdminCatagory(admin.ModelAdmin):
    
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name']
    
class AdminProduct(admin.ModelAdmin):
    
    list_display = ['name', 'slug', 'price', 'category', 'created', 'modified', 'description']
    search_fields = ['name', 'category__name']
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCatagory)

