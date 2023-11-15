from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def displayView(request):
    if request.method=="GET":
        return HttpResponse(json.dumps({"status":"Hello"}))

def addStudentView(request):
    if request.method == "GET":
        return HttpResponse(json.dumps({"status":"Student adding section"}))
    
def searchStudentView(request):
    if request.method == "GET":
        return HttpResponse(json.dumps({"status":"Student Searching section"}))
    
def deleteStudentView(request):
    if request.method == "GET":
        return HttpResponse(json.dumps({"status":"Student Delete section"}))