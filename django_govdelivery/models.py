from django.db import models

# Create your models here.


class SubscriptionAttempt(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    email_address = models.EmailField()
    topics_json = models.TextField(blank=True)
    exception_type= models.CharField(max_length=1000, blank=True)
    exception_message = models.TextField(blank=True)
    success = models.BooleanField(default=False)
