from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from movies.serializer import MovieSerializer
from .models import MovieAdd

# Create your views here.
@csrf_exempt
def displayView(request):
    if request.method=="POST":
        movieList = MovieAdd.objects.all()
        serialize_data = MovieSerializer(movieList,many=True)
        return HttpResponse(json.dumps(serialize_data.data))
    
@csrf_exempt    
def addView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        print(data)
        print(json.dumps(data))
        movie_serializer=MovieSerializer(data=data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return HttpResponse(json.dumps({"status":"success in adding movie data"}))
        else:
            return HttpResponse(json.dumps({
            "status":"No Data Added to movies collection"
        }))
    
@csrf_exempt    
def searchView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({
            "status":"Movies Search"
        }))
    
@csrf_exempt    
def deleteView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({
            "status":"Movies Delete"
        }))