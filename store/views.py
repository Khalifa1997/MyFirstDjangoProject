from django.views import generic
from .models import product, company
import django_filters

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    company = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = product
        fields = ['name', 'company', ]


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
