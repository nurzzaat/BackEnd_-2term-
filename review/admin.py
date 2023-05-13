from django.contrib import admin
from review.models import (Artist, Album, Song, PlaylistSong, Playlist)


def initialled_name(obj):
    """ obj.first_names='Jerome David', obj.last_names='Salinger'
        => 'Salinger, JD' """
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)


# Register your models here.

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(PlaylistSong)

admin.site.register(Album)
