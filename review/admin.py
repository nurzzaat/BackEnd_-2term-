from django.contrib import admin
from review.models import (User, Artist, Album, Song, PlaylistSong, Playlist)

# Register your models here.
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(PlaylistSong)
admin.site.register(Album)
