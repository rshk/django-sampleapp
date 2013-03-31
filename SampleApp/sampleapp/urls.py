from django.conf.urls import patterns, include, url
from .views import ListObjView, CreateObjView, DetailObjView, UpdateObjView, DeleteObjView

urlpatterns = patterns('',
    url(r'^$', ListObjView.as_view(), name='list'),
    url(r'^create/?$',             CreateObjView.as_view(), name='create'),
    url(r'^detail/(?P<pk>\d+)/?$', DetailObjView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/?$', UpdateObjView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/?$', DeleteObjView.as_view(), name='delete'),
)
