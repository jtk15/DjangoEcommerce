from django.shortcuts import render
from .models import Product, Category
from django.http import HttpResponse



def product_list(request):
    
    context = {
        'products': Product.objects.all()
    }
    
    return render(request, 'catalog/products.html', context=context)


def category_product_list(request, category):
    
    print(category)
    
    
    products = Product.objects.filter(category__slug=category)
    
    category = Category.objects.get(slug=category)
    
    context = {
        'products': Product.objects.filter(category=category)
    }
   
    return render(request, 'catalog/bycategory.html', context)


def one_product_list(request, slug):
    
    product = Product.objects.get(slug=slug)
    
    context = {
        'product': product
    }
    
    return render(request, 'catalog/detailproduct.html', context)
    