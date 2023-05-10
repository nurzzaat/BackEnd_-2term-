from django.shortcuts import render, get_object_or_404

from .models import (User, Artist, Album, Song, Playlist, PlaylistSong)


def index(request):
    return render(request, "base.html", {'registered': registered})


registered = True

def album_list(request):
    albums = Album.objects.all()
    albums_with_genre = {}

    for album in albums:
        if album.genre not in albums_with_genre:
            albums_with_genre[album.genre] = []
        albums_with_genre[album.genre].append(album)


    return render(request, "album_list.html", {'albums_with_genre': albums_with_genre})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    # print(album.name)
    songs = Song.objects.filter(album__name=album.name)
    # print(songs)

    return render(request, "album_songs.html", {'songs': songs, 'album': album})

def genre_list(request):
    albums = Album.objects.all()
    genre_set = set()

    for album in albums:
        if len(genre_set) == 4:
            break
        genre_set.add(album.genre)

    return render(request, "search.html", {'genre_set': genre_set})

def albums_in_genre(request, genre_name):
    albums = Album.objects.all()
    albums_of_one_genre = []

    print("rbrbrtb")
    for album in albums:
        if genre_name == album.genre:
            albums_of_one_genre.append(album)

    return render(request, "albums_of_one_genre.html", {'genre': genre_name, 'albums_of_one_genre': albums_of_one_genre})


def songs_detail(request, album_name, pk):
    song = Song.objects.get(pk=pk)
    list_of_songs = []
    list_of_songs.append(song)

    return render(request, "song_detail.html", {'list_of_songs': list_of_songs})

def get_songs(request, song_name):
    songs = Song.objects.all()
    list_of_songs = []

    for song in songs:
        if song.name == song_name:
            list_of_songs.append(song)

    return render(request, "song_detail.html", {'list_of_songs': list_of_songs})

