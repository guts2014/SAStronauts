from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    (r'^$', 'index_page'),
)
