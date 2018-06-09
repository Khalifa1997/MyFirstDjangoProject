from django.views import generic
from .models import product, company

class IndexView(generic.ListView):
    template_name = 'store/store.html'
    context_object_name = 'products'
    def get_queryset(self):
        return product.objects.all()


class ProductsDetailView(generic.DetailView):
    template_name='store/storeDetails.html'
    context_object_name = 'product'
    
    def get_queryset(self):
        return product.objects.all()

class FilterDetailView(generic.DetailView):
    template_name='store/storeDetails.html'
    context_object_name = 'product'
    
    def get_queryset(self):
        return product.objects.all()
