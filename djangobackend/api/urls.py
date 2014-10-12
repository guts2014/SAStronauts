from django.conf.urls import patterns, include, url

#To make a call to the api, we should do /api/<'context' or 'query'>/?q=some+query
urlpatterns = patterns('api.views',
    (r'^test/', 'api_test'),
    (r'^query/$', 'api_query'),
    (r'^context/', 'api_context'),
    (r'^info/', 'api_info'),
    (r'^$', 'api_call'),
)
