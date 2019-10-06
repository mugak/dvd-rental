from django.contrib import admin
from catalog.models import Movie, Genre, MovieInstance, Actor, Language, Director

#admin.site.register(Movie)
admin.site.register(Genre)
#admin.site.register(MovieInstance)
#admin.site.register(Actor)
admin.site.register(Language)
admin.site.register(Director)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'middle_name', 'last_name'), ('date_of_birth', 'date_of_death')]

class MovieInstanceInline(admin.TabularInline):
    model = MovieInstance
    extra = 0

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    inlines = [MovieInstanceInline]

@admin.register(MovieInstance)
class MovieInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_date')
    fieldsets = (
        (None, {'fields': ('movie', 'id')}),
        ('Availability', {'fields': ('status', 'due_date')}),
    )
