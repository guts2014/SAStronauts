from django.conf.urls import patterns, include, url
from django.contrib import admin

#We redirect all api requests on to the api app, and all requests to the main page to the main app.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangobackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^api/', include('api.urls')),
    (r'^$', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
