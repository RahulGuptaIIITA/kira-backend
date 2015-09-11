# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'question_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'question', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'question_question')


    models = {
        u'question.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['question']