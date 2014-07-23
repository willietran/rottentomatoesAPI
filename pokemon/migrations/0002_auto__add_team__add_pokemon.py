# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'pokemon_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'pokemon', ['Team'])

        # Adding model 'Pokemon'
        db.create_table(u'pokemon_pokemon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('pokedex_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pokemon.Team'])),
        ))
        db.send_create_signal(u'pokemon', ['Pokemon'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'pokemon_team')

        # Deleting model 'Pokemon'
        db.delete_table(u'pokemon_pokemon')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['pokemon']