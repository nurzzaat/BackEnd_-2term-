from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('albums/', views.album_list),
    path('search-page/', views.genre_list),
    path('<str:name>', views.search_song, name='search_results'),
    path('albums/<int:pk>/', views.album_detail),
    path('genre/<str:genre_name>/', views.albums_in_genre),
    path('albums/<str:album_name>/<int:pk>/', views.songs_detail)
]
