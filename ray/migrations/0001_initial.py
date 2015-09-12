# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Doctor'
        db.create_table(u'ray_doctor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'ray', ['Doctor'])

        # Adding model 'Appointment'
        db.create_table(u'ray_appointment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ray.Doctor'])),
            ('treatmentPlanName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cancelled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cancelled_reason', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('scheduled_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('scheduled_till', self.gf('django.db.models.fields.DateTimeField')()),
            ('photo_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('has_photo', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ray', ['Appointment'])

        # Adding model 'Prescription'
        db.create_table(u'ray_prescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appointment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ray.Appointment'])),
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dosage', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'ray', ['Prescription'])


    def backwards(self, orm):
        # Deleting model 'Doctor'
        db.delete_table(u'ray_doctor')

        # Deleting model 'Appointment'
        db.delete_table(u'ray_appointment')

        # Deleting model 'Prescription'
        db.delete_table(u'ray_prescription')


    models = {
        u'ray.appointment': {
            'Meta': {'object_name': 'Appointment'},
            'cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cancelled_reason': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ray.Doctor']"}),
            'has_photo': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
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
        u'ray.prescription': {
            'Meta': {'object_name': 'Prescription'},
            'appointment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ray.Appointment']"}),
            'dosage': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ray']