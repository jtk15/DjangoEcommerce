from django.shortcuts import render
from .models import Product


def product_list(request):
    
    context = {
        'products': Product.objects.all()
    }
    
    return render(request, 'catalog/product.html', context=context)