from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('albums/', views.album_list),
    path('search/', views.genre_list),
    path('search/<str:song_name>/', views.get_songs),
    path('albums/<int:pk>/', views.album_detail),
    path('genre/<str:genre_name>/', views.albums_in_genre),
    path('albums/<str:album_name>/<int:pk>/', views.songs_detail)
]
