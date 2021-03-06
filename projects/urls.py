from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProjectIndex.as_view(), name='index'),
    url(r'^new/$', views.CreateProject.as_view(), name='create'),

    url(r'^(?P<pk>[0-9]+)/$',                   views.ProjectDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)-(?P<name>[-_\w]+)/$', views.ProjectDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update$', views.ProjectUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.ProjectDelete.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/verify$', views.ProjectVerify.as_view(), name='verify'),

    url(r'^tag/(?P<tag>[-_\w]+)/$', views.ProjectIndexByTag.as_view(), name='list-by-tag'),

    url(r'^(?P<pk>[0-9]+)/vouch$', views.ProjectVouch.as_view(), name='vouch'),

    url(r'^(?P<pk>[0-9]+)/submissions/create$', views.SubmissionCreate.as_view(), name='create-submission'),
    url(r'^(?P<pk>[0-9]+)-(?P<name>[-_\w]+)/submission/create$', views.SubmissionCreate.as_view(), name='create-submission'),
    url(r'^submissions/(?P<pk>[0-9]+)/verify$', views.SubmissionVerify.as_view(), name='verify-submission'),
]
