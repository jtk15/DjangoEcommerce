from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category

from ecommerce.forms import ContactForms


def index(request):
    
    contexts = {
        'title': 'Django Ecommerce',
        'texts': ['Joelton, Marina, Ana Paula'],
        'categories': Category.objects.all()
    }
    
    return render(request, 'index.html')

def contact(request):
    
    form = ContactForms()
    
    context = {
        'form': form
    }
    
    return render(request, 'contact.html', context)

def category(request):
    
    return render(request, 'category.html')


def privacy(request):
    
    return render(request, 'privacy.html')

def product(request):
    
    return render(request, 'product.html')
