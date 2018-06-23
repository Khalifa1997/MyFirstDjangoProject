from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(),name='boards')   
    path('<int:pk>/<int:pk2>', views.ThreadDetailView.as_view(),name='replies')
    path('<int:pk>/', views.BoardDetailView.as_view(),name='threads')    
    
 
]
