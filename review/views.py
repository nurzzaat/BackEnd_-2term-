from django.shortcuts import render, get_object_or_404

from .models import (User, Artist, Album, Song, Playlist, PlaylistSong)


def index(request):
    return render(request, "base.html")


# Create your views here.

def album_list(request):
    albums = Album.objects.all()
    albums_with_genre = {}

    for album in albums:
        if album.genre not in albums_with_genre:
            albums_with_genre[album.genre] = []
        albums_with_genre[album.genre].append(album.name)

    return render(request, "album_list.html", {'albums_with_genre' : albums_with_genre})

