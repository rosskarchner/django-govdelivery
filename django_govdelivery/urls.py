from django.conf.urlsimport *


urlpatterns = patterns('django_govdelivery.views',
    url(r'^new$', 'subscribe'),
)
