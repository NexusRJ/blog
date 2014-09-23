from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogapp.views import archive

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    url(r'^blog/', include('blogapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
