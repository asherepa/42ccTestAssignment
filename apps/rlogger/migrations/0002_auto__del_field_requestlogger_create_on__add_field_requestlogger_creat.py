# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RequestLogger.create_on'
        db.delete_column(u'rlogger_requestlogger', 'create_on')

        # Adding field 'RequestLogger.created_on'
        db.add_column(u'rlogger_requestlogger', 'created_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 16, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'RequestLogger.create_on'
        db.add_column(u'rlogger_requestlogger', 'create_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 16, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'RequestLogger.created_on'
        db.delete_column(u'rlogger_requestlogger', 'created_on')


    models = {
        u'rlogger.requestlogger': {
            'Meta': {'object_name': 'RequestLogger'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['rlogger']