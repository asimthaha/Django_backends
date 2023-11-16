from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializer import *
import json
from django.views.decorators.csrf  import csrf_exempt

# Create your views here.
@csrf_exempt
def addView(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        serialize_data = DoctorSerializer(data=data)
        if serialize_data.is_valid():
            serialize_data.save()
            return HttpResponse(json.dumps({"status":"Doctor data added successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"Doctor data not added"}))
    
@csrf_exempt
def displayView(request):
    if request.method=="POST":
        doctorList=DoctorAddModel.objects.all()
        serializer = DoctorSerializer(doctorList, many=True)
        return HttpResponse(json.dumps(serializer.data))
    
@csrf_exempt
def searchView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"Doctor data search page"}))
    
@csrf_exempt
def deleteView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"Doctor data delete page"}))
    

