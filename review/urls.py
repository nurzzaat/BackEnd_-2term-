from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('albums/', views.album_list)
]
