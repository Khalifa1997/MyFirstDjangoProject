from django.conf.urls import url
from django.urls import path
from . import views
from . import filters
from django_filters.views import FilterView
urlpatterns = [
    path('', views.IndexView.as_view(), name='store'),
    path('search/', FilterView.as_view(filterset_class= filters.ProductFilter ,template_name = 'store/filterList.html'), name='search'),
    path('<int:pk>/',views.ProductsDetailView.as_view(),name='StoreDetails'),
]