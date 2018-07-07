from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(),name='boards'), 
    path('<int:board_id>/<int:thread_id>/', views.ThreadDetailView.as_view(), name='forumreplies'),
    path('<int:pk>/', views.BoardDetailView.as_view(),name='threads'),   
]
