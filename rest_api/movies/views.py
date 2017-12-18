from movies.models import Movie
from movies.serializer import MovieSerializer
from rest_framework import generics


class MoviesView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
