
from django.urls import path
from .views import product_list, category_product_list

urlpatterns = [
    path('produto/', product_list, name='product'),
    path('produto/<str:category>/', category_product_list, name='category')
]
