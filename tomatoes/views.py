import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tomatoes.models import Movie, Favorite

# Create your views here.


# def home(request):
#     return render(request, 'tomatoes_base.html')


@csrf_exempt
def home(request):
    print "in view"
    if request.method == 'POST':
        print "in if"
        data = json.loads(request.body)
        print "Printing Data..."
        print data
        movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],
            critic_rating=data['critic_rating'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            year=data['year'],
            audience_score=data['audience_score']
        )
        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster
        }
        print "Created Movie..."
        response = serializers.serialize('json', [movie])
        return HttpResponse(response, content_type='application/json')
    else:
        return render(request, 'tomatoes_base.html')


@csrf_exempt
def new_movie(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],
            critic_rating=data['critic_rating'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            year=data['year'],
            audience_score=data['audience_score']
        )
        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster
        }
        return render(request, 'movie_template.html', movie_info)


def view_favorite(request):
    if request.method == "GET":
        favorite = Movie.objects.all()
        data = {'favorite': favorite}
        return render(request, "view_favorite.html", data)


@csrf_exempt
def delete_favorite(request):
    if request.method == "POST":
        movie_title = json.loads(request.body)
        delete_movie = Movie.objects.get(title=movie_title).delete()
        favorite = Movie.objects.all()
        data = {'favorite': favorite}
        return render(request, "view_favorite.html", data)


def movie_tinder(request):
    return render(request, "tinder.html")


@csrf_exempt
def new_favorite(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        favorites = Favorite.objects.create(
            title=data['title'],
            poster=data['poster'],
            identifier=data['identifier'],
        )

        movie_info = {
            'title': favorites.title,
            'poster': favorites.poster,
            'identifier': favorites.identifier
        }
        return render(request, "movie_template.html", movie_info)
