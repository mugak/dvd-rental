from django.shortcuts import render
from catalog.models import Movie, Actor, Director, MovieInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_movies = Movie.objects.all().count()
    num_instances = MovieInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = MovieInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_actors = Actor.objects.count()
    
    num_directors = Director.objects.count()

    context = {
        'num_movies': num_movies,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_actors': num_actors,
        'num_directors': num_directors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)