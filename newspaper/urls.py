from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/newComment/$', views.new_comment, name='new_comment'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Delete, name='delete'),
    url(r'^(?P<pk>[0-9]+)/$',views.ArticleDetailsView.as_view(),name='articledetails'),
    url(r'^new/$', views.new_article, name='new_article'),
]
