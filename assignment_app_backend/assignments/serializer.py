from rest_framework import serializers
from .models import *

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentAddModel
        fields=(
            'name','subject','teacher','description','fileType', 'lastDate'
        )