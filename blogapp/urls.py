from django.conf.urls import patterns, include, url
from django.http import request
from blogapp.views import archive, about,books,codes,showblog,comment

urlpatterns = patterns('',
        url(r'^$',archive),
        url(r'^books/',books),
        url(r'^codes/',codes),
        url(r'^about/',about),
        url(r'^(.*)/',showblog,name='showblog'),
        url(r'^comment',comment),
)