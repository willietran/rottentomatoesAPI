from django.contrib import admin
from pokemon.models import *

# Register your models here.
from tomatoes.models import Favorite


admin.site.register(Pokemon)
admin.site.register(Team)

admin.site.register(Favorite)
