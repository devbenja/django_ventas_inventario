from django.shortcuts import render
from .models import Category
from django.views.generic import ListView


def home_view(request):
    """
        Home View.
        return: template.
    """
    
    return render(request, 'inventory/inicio.html')
    

class CategoryListView(ListView):
    
    model = Category
    template_name = 'category/category_list.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.all()
        
        context['title'] = 'Categorias'
        
        context['accion'] = {
            'accion_uno': 'Listado de Categorias',
            'accion_dos': 'Crear Categoria'
        }
        
        return context