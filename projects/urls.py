from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProjectIndex.as_view(), name='index'),
    url(r'^new/$', views.CreateProject.as_view(), name='create'),

    url(r'^(?P<pk>[0-9]+)-(?P<name>[-_\w]+)/detail$', views.ProjectDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/verify$', views.verify, name='verify'),

    url(r'^tag/(?P<tag>[-_\w]+)/$', views.ProjectIndexByTag.as_view(), name='list-by-tag'),
]