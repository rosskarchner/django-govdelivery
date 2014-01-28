import sys
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

from govdelivery.api import GovDelivery

from .models import SubscriptionAttempt

ACCOUNT_CODE = settings.GOVDELIVERY_ACCOUNT_CODE
gd = GovDelivery(account_code=ACCOUNT_CODE)


def fail_with_code_and_message(code, message):
    response = HttpResponse(message)
    response.status_code = code
    return response

def fail_with_missing_parameter(missing_parameter):
    text = 'Required parameter "%s" is missing' % missing_parameter
    response = fail_with_code_and_message(400, text)
    return response

def extract_answers_from_request(request):
    answers=[]
    for param, value in request.POST.items():
        if param.startswith('questionid'):
            question_id = param.split('_')[1]
            answers.append((question_id,value))
    return answers

@csrf_exempt
def subscribe(request):

    if request.method == 'POST':
        for required_param in ['email','code']:
            if required_param not in request.POST:
                return fail_with_missing_parameter(required_param)

        email_address = request.POST['email']
        codes = request.POST.getlist('code')
        sa = SubscriptionAttempt(email_address=email_address, topics_json=json.dumps(codes))
        sa.save()
        try:
            subscription_response = gd.set_subscriber_topics(email_address, codes)
            if subscription_response.status_code == 200:
                sa.success=True
                sa.save()
            else:
                return fail_with_code_and_message(500, "subscription attempt failed")
        except Exception, e:
            sa.exception_type = unicode(type(e))
            sa.exception_message = e.message
            sa.save()
            return fail_with_code_and_message(500, "subscription attempt failed")


        answers = extract_answers_from_request(request)
        for question_id, answer_text in answers:
                response = gd.set_subscriber_answers_to_question(email_address, question_id, answer_text)

        return HttpResponse("subscription successful!")
    else:
        return fail_with_code_and_message(405, 'Method not allowed')
