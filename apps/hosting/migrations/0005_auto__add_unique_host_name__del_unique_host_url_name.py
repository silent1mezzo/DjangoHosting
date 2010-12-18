# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Host', fields ['url', 'name']
        db.delete_unique('hosting_host', ['url', 'name'])

        # Adding unique constraint on 'Host', fields ['name']
        db.create_unique('hosting_host', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Host', fields ['name']
        db.delete_unique('hosting_host', ['name'])

        # Adding unique constraint on 'Host', fields ['url', 'name']
        db.create_unique('hosting_host', ['url', 'name'])


    models = {
        'hosting.host': {
            'Meta': {'object_name': 'Host'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desription': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'referral_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'small_image_one': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image_two': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hosting.HostType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'hosting.hosttype': {
            'Meta': {'object_name': 'HostType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hosting']
