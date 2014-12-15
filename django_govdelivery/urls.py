from django.conf.urls import *


urlpatterns = patterns('django_govdelivery.views',
    url(r'^new$', 'subscribe'),
)
