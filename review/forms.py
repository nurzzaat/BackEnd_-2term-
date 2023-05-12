from django import forms
from .models import Song


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=2)
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("Song", "Song"),
                                      ("Artist", "Artist")))



class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'artist', 'album', 'length']
        labels = {
            'name': 'Song Name',
            'length': 'Length (in seconds)',
            'artist': 'Artist Name',
            'album': 'Album Name'
        }
