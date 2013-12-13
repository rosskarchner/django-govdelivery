from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

from govdelivery.api import GovDelivery

ACCOUNT_CODE = settings.GOVDELIVERY_ACCOUNT_CODE
gd = GovDelivery(account_code=ACCOUNT_CODE)


@csrf_exempt
def subscribe(request):
    if request.method == 'POST' and 'email' in request.POST:
        email_address = request.POST['email']
        gd.create_subscriber(email_address)

        codes = request.POST.getlist('code')
        gd.set_subscriber_topics(email_address, codes)
        return HttpResponse("subscription successful!")
