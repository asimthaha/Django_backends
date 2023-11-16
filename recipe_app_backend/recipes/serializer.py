from rest_framework import serializers
from .models import *

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeAddModel
        fields =(
            'name','author','dateCreated','ingredients','description','type'
        )