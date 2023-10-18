from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def first_view(request):
    
    data = {
        'ABA': 'United States',
        'ORG': 'Spain'
    }
    return JsonResponse(data) 
