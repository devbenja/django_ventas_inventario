from django.shortcuts import render

def first_view(request):
    return render(request, 'inventory/inicio.html')
