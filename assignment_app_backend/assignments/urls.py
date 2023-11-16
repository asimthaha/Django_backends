from django.urls import path
from . import views


urlpatterns = [
    path('view/',views.displayView, name="view"),
    path('add/', views.addView, name="add"),
    path('search/',views.searchView, name="search"),
    path('delete/', views.deleteView, name="delete")
]
