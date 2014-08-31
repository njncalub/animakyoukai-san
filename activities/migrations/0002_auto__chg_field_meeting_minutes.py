# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Meeting.minutes'
        db.alter_column(u'activities_meeting', 'minutes', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True))

    def backwards(self, orm):

        # Changing field 'Meeting.minutes'
        db.alter_column(u'activities_meeting', 'minutes', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True))

    models = {
        u'activities.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'minutes': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['activities']