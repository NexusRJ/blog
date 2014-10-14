from django.conf.urls import patterns, include, url
from django.contrib import admin
import os
#from blogapp.views import archive,home

#admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^', include('blogapp.urls')),
)