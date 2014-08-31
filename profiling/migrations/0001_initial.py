# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'profiling_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('nick_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('landline_number', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=200, null=True, blank=True)),
            ('website_address', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('application_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('member_status', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'profiling', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'profiling_person')


    models = {
        u'profiling.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'application_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landline_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'member_status': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'website_address': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiling']