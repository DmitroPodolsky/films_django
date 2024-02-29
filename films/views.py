from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Actor
from .models import Director
from .models import Movie
from .serializers import ActorSerializer
from .serializers import DirectorSerializer
from .serializers import MovieSerializer
from films.filters import MovieFilter


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]


class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
