from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:product_id>/',remove_from_cart,name='remove_from_cart'),
    path('item_list/', item_list, name='item_list'),
]