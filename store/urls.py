from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='store'),
    path('<int:pk>/',views.ProductsDetailView.as_view(),name='StoreDetails'),

]