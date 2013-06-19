# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestsLogger'
        db.create_table(u'rlogger_requestslogger', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal(u'rlogger', ['RequestsLogger'])


    def backwards(self, orm):
        # Deleting model 'RequestsLogger'
        db.delete_table(u'rlogger_requestslogger')


    models = {
        u'rlogger.requestslogger': {
            'Meta': {'object_name': 'RequestsLogger'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['rlogger']