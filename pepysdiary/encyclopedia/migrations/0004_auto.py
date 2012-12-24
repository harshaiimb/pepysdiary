# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field categories on 'Topic'
        db.create_table('encyclopedia_topic_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('topic', models.ForeignKey(orm['encyclopedia.topic'], null=False)),
            ('category', models.ForeignKey(orm['encyclopedia.category'], null=False))
        ))
        db.create_unique('encyclopedia_topic_categories', ['topic_id', 'category_id'])


    def backwards(self, orm):
        # Removing M2M table for field categories on 'Topic'
        db.delete_table('encyclopedia_topic_categories')


    models = {
        'encyclopedia.category': {
            'Meta': {'object_name': 'Category'},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'encyclopedia.topic': {
            'Meta': {'ordering': "['title']", 'object_name': 'Topic'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'topics'", 'symmetrical': 'False', 'to': "orm['encyclopedia.Category']"}),
            'comment_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '6', 'blank': 'True'}),
            'map_category': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'order_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'shape': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'summary_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tooltip_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'wheatley': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'wheatley_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'wikipedia_fragment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zoom': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['encyclopedia']