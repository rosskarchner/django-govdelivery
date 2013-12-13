from django.conf.urls.defaults import *


urlpatterns = patterns('django_govdelivery.views',
    url(r'^new$', 'subscribe'),
)
