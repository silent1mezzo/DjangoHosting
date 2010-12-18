# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Host'
        db.create_table('hosting_host', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('desription', self.gf('django.db.models.fields.TextField')()),
            ('large_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('small_image_one', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('small_image_two', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('hosting', ['Host'])

        # Adding unique constraint on 'Host', fields ['name', 'url']
        db.create_unique('hosting_host', ['name', 'url'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Host', fields ['name', 'url']
        db.delete_unique('hosting_host', ['name', 'url'])

        # Deleting model 'Host'
        db.delete_table('hosting_host')


    models = {
        'hosting.host': {
            'Meta': {'unique_together': "(('name', 'url'),)", 'object_name': 'Host'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desription': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'small_image_one': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image_two': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hosting']
