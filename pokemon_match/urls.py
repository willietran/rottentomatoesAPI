from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from pokemon_match import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokemon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^all_pokemon/$', 'pokemon.views.all_pokemon', name='all_pokemon'),
    url(r'^view_pokemon/$', 'pokemon.views.view_pokemon', name='view_pokemon'),
    url(r'^new_pokemon/$', 'pokemon.views.new_team', name='new_pokemon'),
    url(r'^pokemon_info/(?P<pokemon_id>\w+)/$', 'pokemon.views.pokemon_info', name='pokemon_info'),

    #URLs for Rotten Tomatoes
    url(r'^$', 'tomatoes.views.home', name='home'),
    url(r'^new_movie/$', 'tomatoes.views.new_movie', name='new_movie'),
    url(r'^view_favorite/$', 'tomatoes.views.view_favorite', name='view_favorite'),
    url(r'^delete_favorite/$', 'tomatoes.views.delete_favorite', name='delete_favorite'),
    # url(r'^favorites/$', 'tomatoes.views.favorite', name='favorite'),


    #URLs for Tinder
    url(r'^movie_tinder/$', 'tomatoes.views.movie_tinder', name='movie_tinder'),
    url(r'^new_favorite/$', 'tomatoes.views.new_favorite', name='new_favorite'),



)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)