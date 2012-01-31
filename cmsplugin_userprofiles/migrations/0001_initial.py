# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserSettings'
        db.create_table('cmsplugin_usersettings', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('group_title', self.gf('django.db.models.fields.CharField')(default='Users', max_length=128)),
        ))
        db.send_create_signal('cmsplugin_userprofile', ['UserSettings'])

        # Adding model 'GroupSettings'
        db.create_table('cmsplugin_groupsettings', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('group_title', self.gf('django.db.models.fields.CharField')(default='Users', max_length=128)),
            ('operator', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('container_template', self.gf('django.db.models.fields.CharField')(default=('default', 'cmsplugin_userprofile/list/container/default.html'), max_length=256, null=True, blank=True)),
            ('item_template', self.gf('django.db.models.fields.CharField')(default='cmsplugin_userprofile/list/item/default.html', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('cmsplugin_userprofile', ['GroupSettings'])

        # Adding M2M table for field groups on 'GroupSettings'
        db.create_table('cmsplugin_userprofile_groupsettings_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('groupsettings', models.ForeignKey(orm['cmsplugin_userprofile.groupsettings'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('cmsplugin_userprofile_groupsettings_groups', ['groupsettings_id', 'group_id'])


    def backwards(self, orm):
        
        # Deleting model 'UserSettings'
        db.delete_table('cmsplugin_usersettings')

        # Deleting model 'GroupSettings'
        db.delete_table('cmsplugin_groupsettings')

        # Removing M2M table for field groups on 'GroupSettings'
        db.delete_table('cmsplugin_userprofile_groupsettings_groups')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_userprofile.groupsettings': {
            'Meta': {'object_name': 'GroupSettings', 'db_table': "'cmsplugin_groupsettings'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'container_template': ('django.db.models.fields.CharField', [], {'default': "('default', 'cmsplugin_userprofile/list/container/default.html')", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'group_title': ('django.db.models.fields.CharField', [], {'default': "'Users'", 'max_length': '128'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'item_template': ('django.db.models.fields.CharField', [], {'default': "'cmsplugin_userprofile/list/item/default.html'", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'operator': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'cmsplugin_userprofile.usersettings': {
            'Meta': {'object_name': 'UserSettings', 'db_table': "'cmsplugin_usersettings'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'group_title': ('django.db.models.fields.CharField', [], {'default': "'Users'", 'max_length': '128'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cmsplugin_userprofile']
