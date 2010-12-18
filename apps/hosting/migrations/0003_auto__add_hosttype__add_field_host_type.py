# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HostType'
        db.create_table('hosting_hosttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('hosting', ['HostType'])

        # Adding field 'Host.type'
        db.add_column('hosting_host', 'type', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['hosting.HostType']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'HostType'
        db.delete_table('hosting_hosttype')

        # Deleting field 'Host.type'
        db.delete_column('hosting_host', 'type_id')


    models = {
        'hosting.host': {
            'Meta': {'unique_together': "(('name', 'url'),)", 'object_name': 'Host'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desription': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
