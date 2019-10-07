from django.shortcuts import render
from catalog.models import Movie, Actor, Director, MovieInstance, Genre
from django.views import generic

from rest_framework import viewsets
from catalog.serializers import MovieSerializer, MovieInstanceSerializer

class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 10
    
class MovieDetailView(generic.DetailView):
    model = Movie
    
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

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_movies': num_movies,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_actors': num_actors,
        'num_directors': num_directors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieInstanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MovieInstance.objects.all()
    serializer_class = MovieInstanceSerializer