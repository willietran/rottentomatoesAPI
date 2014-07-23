# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Team.name'
        db.delete_column(u'pokemon_team', 'name')

        # Adding field 'Team.type'
        db.add_column(u'pokemon_team', 'type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Team.name'
        db.add_column(u'pokemon_team', 'name',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=30),
                      keep_default=False)

        # Deleting field 'Team.type'
        db.delete_column(u'pokemon_team', 'type')


    models = {
        u'pokemon.pokemon': {
            'Meta': {'object_name': 'Pokemon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pokedex_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pokemon.Team']"})
        },
        u'pokemon.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['pokemon']