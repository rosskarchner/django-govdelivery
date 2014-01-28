# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubscriptionAttempt'
        db.create_table(u'django_govdelivery_subscriptionattempt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('topics_json', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('categories_json', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('qa_json', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'django_govdelivery', ['SubscriptionAttempt'])


    def backwards(self, orm):
        # Deleting model 'SubscriptionAttempt'
        db.delete_table(u'django_govdelivery_subscriptionattempt')


    models = {
        u'django_govdelivery.subscriptionattempt': {
            'Meta': {'object_name': 'SubscriptionAttempt'},
            'categories_json': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qa_json': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'topics_json': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['django_govdelivery']