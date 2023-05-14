from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.album_list),
    path('accounts/profile/', views.profile, name='profile'),
    path('login/', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path("logout_user", views.logout_user, name="logout"),
    path('albums/', views.album_list, name='albums'),
    path('search/', views.genre_list, name='song_search'),
    path('albums/<int:pk>/', views.album_detail),
    path('genre/<str:genre_name>/', views.albums_in_genre),
    path('song/<int:pk>/', views.songs_detail, name='song_detail'),
    path('songedit/<int:song_pk>/', views.song_edit, name='song_edit'),
    path('my_library/', views.my_library, name='my_library'),
    path('add_song_to_playlist/<int:pk>', views.add_song_to_playlist, name='add_song_to_playlist'),
    path('playlist/<int:pk>', views.playlist_detail, name='playlist_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
