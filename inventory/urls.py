from django.urls import path 
from .views import *

urlpatterns = [
    path('testing_url/', first_view, name='testing')
]
