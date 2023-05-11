from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('albums/', views.album_list, name='albums'),
    path('search-page/', views.genre_list),
    path('<str:name>', views.search_song, name='search_results'),
    path('albums/<int:pk>/', views.album_detail),
    path('genre/<str:genre_name>/', views.albums_in_genre),
    path('albums/<str:album_name>/<int:pk>/', views.songs_detail),
    path('songedit/<int:song_pk>/', views.song_edit, name='song_edit'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
