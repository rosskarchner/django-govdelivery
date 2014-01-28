# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SubscriptionAttempt.sucess'
        db.delete_column(u'django_govdelivery_subscriptionattempt', 'sucess')

        # Adding field 'SubscriptionAttempt.success'
        db.add_column(u'django_govdelivery_subscriptionattempt', 'success',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SubscriptionAttempt.sucess'
        db.add_column(u'django_govdelivery_subscriptionattempt', 'sucess',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'SubscriptionAttempt.success'
        db.delete_column(u'django_govdelivery_subscriptionattempt', 'success')


    models = {
        u'django_govdelivery.subscriptionattempt': {
            'Meta': {'object_name': 'SubscriptionAttempt'},
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'topics_json': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['django_govdelivery']