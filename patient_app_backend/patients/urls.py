from django.urls import path,include
from . import views

urlpatterns = [
    path('add/', views.addView, name="add"),
    path('view/', views.displayView, name="view"),
    path('search/', views.searchView, name="search"),
    path('delete/', views.deleteView, name="delete"),
]