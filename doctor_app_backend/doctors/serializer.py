from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAddModel
        fields=(
            'name','qualification','specialization','address','department','salary'
        )