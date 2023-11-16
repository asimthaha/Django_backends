from rest_framework import serializers
from movies.models import MovieAdd

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieAdd
        fields = ('name', 'actor','actress','director','producer')