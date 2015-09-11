# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Appointment.start'
        db.delete_column(u'ray_appointment', 'start')

        # Adding field 'Appointment.scheduled_at'
        db.add_column(u'ray_appointment', 'scheduled_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2015, 9, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Appointment.scheduled_till'
        db.add_column(u'ray_appointment', 'scheduled_till',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 9, 11, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Appointment.start'
        db.add_column(u'ray_appointment', 'start',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2015, 9, 11, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Appointment.scheduled_at'
        db.delete_column(u'ray_appointment', 'scheduled_at')

        # Deleting field 'Appointment.scheduled_till'
        db.delete_column(u'ray_appointment', 'scheduled_till')


    models = {
        u'ray.appointment': {
            'Meta': {'object_name': 'Appointment'},
            'cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cancelled_reason': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ray.Doctor']"}),
            'has_photo': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ray.Patient']"}),
            'photo_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scheduled_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'scheduled_till': ('django.db.models.fields.DateTimeField', [], {}),
            'treatmentPlanName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'ray.doctor': {
            'Meta': {'object_name': 'Doctor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'ray.patient': {
            'Meta': {'object_name': 'Patient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'ray.prescription': {
            'Meta': {'object_name': 'Prescription'},
            'appointment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ray.Appointment']"}),
            'dosage': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ray']