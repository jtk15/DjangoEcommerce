from django.urls import path


from ecommerce.views import index, contact, category, privacy, product


urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('category/', category),
    path('privacy/', privacy),
    path('product/', product),
]