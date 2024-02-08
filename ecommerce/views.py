from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category

# Create your views here.


def index(request):
    
    contexts = {
        'title': 'Django Ecommerce',
        'texts': ['Joelton, Marina, Ana Paula'],
        'categories': Category.objects.all()
    }
    
    return render(request, 'index.html')

def contact(request):
    
    return render(request, 'contact.html')

def category(request):
    
    return render(request, 'category.html')


def privacy(request):
    
    return render(request, 'privacy.html')

def product(request):
    
    return render(request, 'product.html')
