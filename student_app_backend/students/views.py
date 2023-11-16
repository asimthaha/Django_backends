from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from students.serializer import StudentSerializer
from .models import StudentModel

# Create your views here.
@csrf_exempt
def displayView(request):
    if request.method=="POST":
        studentList = StudentModel.objects.all()
        serialise_data=StudentSerializer(studentList,many=True)
        return HttpResponse(json.dumps(serialise_data.data))

@csrf_exempt
def addStudentView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        student_serializer= StudentSerializer(data=data)
        if student_serializer.is_valid():
            student_serializer.save()
            return HttpResponse(json.dumps({"status":"Success"}))
        else:   
            return HttpResponse(json.dumps({"status":"Failed"}))

@csrf_exempt   
def searchStudentView(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"status":"Student Searching section"}))

@csrf_exempt   
def deleteStudentView(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"status":"Student Delete section"}))