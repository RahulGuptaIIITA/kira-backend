# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Question.task'
        db.alter_column(u'question_question', 'task', self.gf('django.db.models.fields.CharField')(max_length=2))

    def backwards(self, orm):

        # Changing field 'Question.task'
        db.alter_column(u'question_question', 'task', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        u'question.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['question']