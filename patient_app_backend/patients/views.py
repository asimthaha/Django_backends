from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from patients.serializer import PatientSerializer
from .models import PatientAdd

# Create your views here.
@csrf_exempt
def displayView(request):
    if request.method=="POST":
        PatientList = PatientAdd.objects.all()
        serializers=PatientSerializer(PatientList, many=True)
        return HttpResponse(json.dumps(serializers.data))
    
@csrf_exempt
def addView(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        patient_serializer = PatientSerializer(data=data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return HttpResponse(json.dumps({"status":"Patient data added"}))
        else:
            return HttpResponse(json.dumps({
            "status":"Patient Data Not Added"
        }))
    
@csrf_exempt   
def searchView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({
            "status":"Patient Search"
        }))
    
@csrf_exempt    
def deleteView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({
            "status":"Patient Delete"
        }))