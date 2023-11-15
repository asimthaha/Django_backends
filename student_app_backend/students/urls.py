from django.urls import path
from . import views


urlpatterns = [
    path('view/',views.displayView, name="view"),
    path('add/', views.addStudentView, name="add"),
    path('sarch/',views.searchStudentView, name="search"),
    path('delete/', views.deleteStudentView, name="delete")
]
