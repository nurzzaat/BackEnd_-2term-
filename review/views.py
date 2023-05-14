from django.contrib.auth.decorators import login_required

from .forms import *
from .models import (Artist, Album, Song, Playlist, PlaylistSong)
from django.contrib import messages
from django.contrib.auth.models import auth
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect


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
    songs = Song.objects.filter(album__name=album.name)

    return render(request, "album_songs.html", {'songs': songs, 'album': album})


def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    songs = PlaylistSong.objects.filter(playlist=playlist)

    return render(request, "playlist_songs.html", {'playlist': playlist, 'songs': songs})

def delete_song_from_playlist(request, playlist_pk, song_pk):
    song = PlaylistSong.objects.filter(playlist_id=playlist_pk, song_id=song_pk)
    song.delete()

    playlist = Playlist.objects.get(pk=playlist_pk)
    songs = PlaylistSong.objects.filter(playlist=playlist)

    return render(request, "playlist_songs.html", {'playlist': playlist, 'songs': songs})


def genre_list(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    songs = set()

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "Song"
        if search_in == "Song":
            songs = Song.objects.filter(name__icontains=search)
        else:
            artist_names = Artist.objects.filter(name__icontains=search)

            for artist in artist_names:
                for song in artist.song_set.all():
                    songs.add(song)

    albums = Album.objects.all()
    genre_set = set()

    for album in albums:
        if len(genre_set) == 4:
            break
        genre_set.add(album.genre)

    return render(request, "search.html",
                  {'form': form, "search_text": search_text, "songs": songs, 'genre_set': genre_set})


def albums_in_genre(request, genre_name):
    albums = Album.objects.all()
    albums_of_one_genre = []

    for album in albums:
        if genre_name == album.genre:
            albums_of_one_genre.append(album)

    return render(request, "albums_of_one_genre.html",
                  {'genre': genre_name, 'albums_of_one_genre': albums_of_one_genre})


def songs_detail(request, pk):
    song = Song.objects.get(pk=pk)

    return render(request, "song_detail.html", {'song': song})


def search_song(request, name):
    name = request.GET.get('search')
    songs = Song.objects.all()
    list_of_songs = []

    for song in songs:
        if song.name == name:
            list_of_songs.append(song)

    return render(request, "song_detail.html", {'list_of_songs': list_of_songs})


def song_edit(request, song_pk):
    song = get_object_or_404(Song, pk=song_pk)

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            song_instance = form.save(commit=False)
            if 'cover' in request.FILES:
                song_instance.cover = request.FILES['cover']
            song_instance.save()
            return redirect('song_detail', song_pk)
    else:
        form = SongForm(instance=song)

    return render(request, 'song_edit.html', {'form': form})


@login_required
def my_playlist(request):
    user_playlists = Playlist.objects.filter(user=request.user)
    
    return render(request, 'my_library.html', {'playlists': user_playlists})

def delete_playlist(request, pk):
    playlist = Playlist.objects.get(pk=pk, user=request.user)
    playlist.delete()

    user_playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'my_library.html', {'playlists': user_playlists})



def add_song_to_playlist(request, pk):
    song = Song.objects.get(pk=pk)
    playlists = Playlist.objects.filter(user=request.user)

    if request.method == 'POST':
        playlist_id = request.POST.get('playlist')
        playlist = Playlist.objects.get(pk=playlist_id)
        if not PlaylistSong.objects.filter(playlist=playlist, song=song).exists():
            PlaylistSong.objects.create(playlist=playlist, song=song)
        return redirect('playlist_detail', pk=playlist_id)

    return render(request, 'add_song_to_playlist.html', {'playlists': playlists, 'song': song})


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
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('albums')

@login_required
def profile(request):
    user = request.user
    permissions = user.get_all_permissions()
    return render(request, 'profile.html', {'user': user, 'permissions': permissions})

def create_playlist(request):
    if request.method == 'POST':
        form = PlayListForm(request.POST)
        form.user = request.POST.get('user')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_playlist')
    else:
        form = PlayListForm()
    return render(request, 'create_playlist.html', {'form': form})
