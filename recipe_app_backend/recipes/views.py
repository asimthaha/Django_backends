from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .serializer import *

# Create your views here.
@csrf_exempt
def addView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        recipe_serializer = RecipeSerializer(data=data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return HttpResponse(json.dumps({"status":"New Recipe Data Added"}))
        else:
            return HttpResponse(json.dumps({"status":"Recipe Data Not Added"}))

@csrf_exempt
def searchView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"Recipe Data Search"}))

@csrf_exempt   
def deleteView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"Recipe Data Search"}))

@csrf_exempt    
def displayView(request):
    if request.method=="POST":
        recipeList = RecipeAddModel.objects.all()
        serializer = RecipeSerializer(recipeList, many=True)
        return HttpResponse(json.dumps(serializer.data))