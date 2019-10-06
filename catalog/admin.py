from django.contrib import admin
from catalog.models import Movie, Genre, MovieInstance, Actor, Language, Director

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MovieInstance)
admin.site.register(Actor)
admin.site.register(Language)
admin.site.register(Director)