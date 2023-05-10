from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('albums/', views.album_list),
    path('albums/<int:pk>/', views.album_detail),
    path('albums/<int:album_id>/<int:song_id>/', views.song_detail, name='song_detail')
]
