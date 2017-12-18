from rest_framework import serializers

from movies.models import Movie, Person

class PersonRoleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='person_id')
    name = serializers.ReadOnlyField(source='person_name')
    movie_name = serializers.ReadOnlyField(source='movie_title')

    class Meta:
        model = Person
        fields = ('id', 'name',)


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = PersonSerializer(many=False, read_only=True)
    actors = PersonRoleSerializer(source='movieperson.set', many=True)

    class Meta:
        model = Movie
        fields = ("title", "description", "year", "director", "actors")