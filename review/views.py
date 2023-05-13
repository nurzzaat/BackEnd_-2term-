from .forms import SongForm, RegistrationForm
from .models import (Artist, Album, Song, Playlist, PlaylistSong)
from django.contrib import messages
from django.contrib.auth.models import auth
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    return render(request, "base.html")


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

    for album in albums:
        if genre_name == album.genre:
            albums_of_one_genre.append(album)

    return render(request, "albums_of_one_genre.html",
                  {'genre': genre_name, 'albums_of_one_genre': albums_of_one_genre})


def songs_detail(request, album_name, pk):
    song = Song.objects.get(pk=pk)
    list_of_songs = []
    list_of_songs.append(song)

    return render(request, "song_detail.html", {'list_of_songs': list_of_songs})


def search_song(request, name):
    name = request.GET.get('search')
    songs = Song.objects.all()
    list_of_songs = []

    for song in songs:
        if song.name == name:
            list_of_songs.append(song)

    print(list_of_songs)
    return render(request, "song_detail.html", {'list_of_songs': list_of_songs})


def song_edit(request, song_pk):
    song = Song.objects.get(pk=song_pk)

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('albums')
    else:
        form = SongForm(instance=song)

    return render(request, 'song_edit.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('albums')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('albums')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('albums')
