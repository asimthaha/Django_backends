from rest_framework import serializers
from patients.models import PatientAdd

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAdd
        fields =(
            'name','phone','address','email','pincode'
        )