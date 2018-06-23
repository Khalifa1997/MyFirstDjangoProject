from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(),name='boards')   
    path('<int:board_id>/<int:thread_id>', views.ThreadDetailView.as_view(),name='replies')
    path('<int:board_id>/', views.BoardDetailView.as_view(),name='threads')    
    
 
]
