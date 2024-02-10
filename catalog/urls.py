
from django.urls import path
from .views import product_list, category_product_list, one_product_list

urlpatterns = [
    path('produtos/', product_list, name='product'),
    path('produtos/<str:category>/', category_product_list, name='category'),
    path('produto/<str:slug>/', one_product_list, name='one-product-list')
]
