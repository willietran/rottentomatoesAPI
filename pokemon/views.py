# from django.contrib.sessions import serializers
import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from pokemon.models import Pokemon, Team


def all_pokemon(request):
    pokemon = Pokemon.objects.all()
    data = serializers.serialize('json', pokemon)
    return HttpResponse(data, mimetype='application/json')

@csrf_exempt
def view_pokemon(request):
    pokemon_objects = Pokemon.objects.all()
    collection = []
    for pokemon in pokemon_objects:
        collection.append({
            'pk': pokemon.id,
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'team': {
                'id': pokemon.team.id,
                'type': pokemon.team.type
            }
        })
    return HttpResponse(
        json.dumps(collection),
        content_type='application.json'
    )


@csrf_exempt
def new_pokemon(request):
    print "in view"
    if request.method == 'POST':
        print "in if"
        data = json.loads(request.body)
        print "Printing Data..."
        print data
        pokemon = Pokemon.objects.create(
            name=data['name'],
            image=data['image'],
            pokedex_id=data['pokedex_id'],
            team=Team.objects.get(id=team.id)
        )
        print "Print Pokemon object..."
        response = serializers.serialize('json', [pokemon])
        return HttpResponse(response, content_type='application/json')
    else:
        return render(request, 'new_pokemon.html')


@csrf_exempt
def new_team(request):
    if request.method == 'POST':
        print 'if'
        data = json.loads(request.body)
        new_team_id = Team.objects.last().id + 1
        new_team_name = "new_randomTeam {} ".format(new_team_id)
        print data
        team = Team.objects.create(
            type=new_team_name)
        poke = []
        for pokemon in data:
            poke.append(Pokemon.objects.create(
                name=pokemon['name'],
                image=pokemon['image'],
                pokedex_id=pokemon['id'],
                team=Team.objects.get(id=team.id)
            ))

        response = serializers.serialize('json', poke)
        return HttpResponse(response, content_type='application/json')
    else:
        return render(request, 'new_pokemon.html')


def home(request):
    return render(request, 'base.html')


def pokemon_info(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    this_pokemon = {
        'name': pokemon.name,
        'image': pokemon.image,
        'pokedex_id': pokemon.pokedex_id,
        'team': {
            'id': pokemon.team.id,
            'type': pokemon.team.type
        }
    }
    return render(request, 'pokemon_info.html', this_pokemon)

