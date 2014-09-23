from django.conf.urls import patterns,include,url
from blogapp.views import archive

urlpatterns = patterns('',
        url(r'^$',archive),
)