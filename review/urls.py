from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('login/', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path("logout_user", views.logout_user, name="logout"),
    path('albums/', views.album_list, name='albums'),
    path('search/', views.genre_list, name='song_search'),
    # path('search/<int:pk>', views.songs_detail_for_search, name='song_detail'),
    path('albums/<int:pk>/', views.album_detail),
    path('genre/<str:genre_name>/', views.albums_in_genre),
    path('song/<int:pk>/', views.songs_detail, name='song_detail'),
    path('songedit/<int:song_pk>/', views.song_edit, name='song_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
