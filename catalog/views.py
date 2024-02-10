from django.shortcuts import render
from .models import Product, Category
from django.http import HttpResponse



def product_list(request):
    
    context = {
        'products': Product.objects.all()
    }
    
    return render(request, 'catalog/product.html', context=context)


def category_product_list(request, category):
    
    print(category)
    
    
    products = Product.objects.filter(category__slug=category)
    
    category = Category.objects.get(slug=category)
    
    context = {
        'products': Product.objects.filter(category=category)
    }
   
    return render(request, 'bycategory.html', context)
    