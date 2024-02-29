from rest_framework import serializers

from .models import Actor
from .models import Director
from .models import Movie


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "release_year", "director", "actors"]

    def create(self, validated_data):
        director_data = validated_data.pop("director")
        director, _ = Director.objects.get_or_create(**director_data)
        actors_data = validated_data.pop("actors")
        movie = Movie.objects.create(director=director, **validated_data)
        for actor_data in actors_data:
            actor, _ = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)
        return movie
