from django.urls import path 
from .views import *

# Inventory List

urlpatterns = [
    path('', home_view, name='home_view'),
    path('inventory/category/list/', CategoryListView.as_view(), name='category_list'),       
]
