from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='store'),
    url(r'^(?P<pk>\d+)$',views.ProductsDetailView.as_view(),name='StoreDetails'),

]