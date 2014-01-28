# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SubscriptionAttempt.exception_type'
        db.add_column(u'django_govdelivery_subscriptionattempt', 'exception_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000, blank=True),
                      keep_default=False)

        # Adding field 'SubscriptionAttempt.exception_message'
        db.add_column(u'django_govdelivery_subscriptionattempt', 'exception_message',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SubscriptionAttempt.exception_type'
        db.delete_column(u'django_govdelivery_subscriptionattempt', 'exception_type')

        # Deleting field 'SubscriptionAttempt.exception_message'
        db.delete_column(u'django_govdelivery_subscriptionattempt', 'exception_message')


    models = {
        u'django_govdelivery.subscriptionattempt': {
            'Meta': {'object_name': 'SubscriptionAttempt'},
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'exception_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exception_type': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'topics_json': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['django_govdelivery']