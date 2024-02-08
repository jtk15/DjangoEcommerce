from django.urls import path


from ecommerce.views import index, contact, category, privacy, product


urlpatterns = [
    path('', index, name='start'),
    path('contato', contact, name='contact'),
    path('categoria', category, name='category'),
    path('privacidade', privacy, name='privacy'),
]