# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestLogger'
        db.create_table(u'rlogger_requestlogger', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal(u'rlogger', ['RequestLogger'])


    def backwards(self, orm):
        # Deleting model 'RequestLogger'
        db.delete_table(u'rlogger_requestlogger')


    models = {
        u'rlogger.requestlogger': {
            'Meta': {'object_name': 'RequestLogger'},
            'create_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['rlogger']