from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    
    contexts = {
        'title': 'Django Ecommerce',
        'texts': ['Joelton, Marina, Ana Paula']
    }
    
    return render(request, 'index.html', contexts)
