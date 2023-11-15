from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def displayView(request):
    if request.method=="GET":
        return HttpResponse(json.dumps({
            "name":"John Doe",
            "age":30,
        }))
    
def addView(request):
    if request.method=="GET":
        return HttpResponse(json.dumps({
            "status":"Patient Add"
        }))
    
def searchView(request):
    if request.method=="GET":
        return HttpResponse(json.dumps({
            "status":"Patient Search"
        }))
    
def deleteView(request):
    if request.method=="GET":
        return HttpResponse(json.dumps({
            "status":"Patient Delete"
        }))