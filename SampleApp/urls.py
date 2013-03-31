from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/sample/')),
    url(r'^sample/', include('SampleApp.sampleapp.urls', namespace='sample', app_name='sample')),
    url(r'^admin/', include(admin.site.urls)),
)
