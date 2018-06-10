from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/newComment/', views.new_comment, name='new_comment'),
    path('<int:pk>/delete/', views.Delete, name='delete'),
    path('<int:pk>/',views.ArticleDetailsView.as_view(),name='articledetails'),
    
    path('new/', views.new_article, name='new_article'),
]
