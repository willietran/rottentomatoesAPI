# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Favorite.identifier'
        db.alter_column(u'tomatoes_favorite', 'identifier', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

    def backwards(self, orm):

        # Changing field 'Favorite.identifier'
        db.alter_column(u'tomatoes_favorite', 'identifier', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

    models = {
        u'tomatoes.favorite': {
            'Meta': {'object_name': 'Favorite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'audience_score': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'critic_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'runtime': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['tomatoes']