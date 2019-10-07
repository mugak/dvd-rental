from catalog.models import Movie, MovieInstance
from rest_framework import serializers

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'synopsis', 'year', 'rating']

class MovieInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieInstance
        fields = ['id', 'movie', 'due_date', 'status']