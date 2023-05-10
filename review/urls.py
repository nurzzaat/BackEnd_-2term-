from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('albums/', views.album_list),
    path('search/', views.genre_list),
    path('albums/<int:pk>/', views.album_detail),
]
