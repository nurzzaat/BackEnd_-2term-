from django import forms
from .models import Song


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=2)
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("Song", "Song"),
                                      ("Artist", "Artist")),
                                  widget=forms.Select(attrs={
                                      'class': 'my-select-class',
                                      'style': 'width: 250px; height: 30px; border: 1px solid #ccc; border-radius: 4px; padding: 5px; font-size: 16px; box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);'
                                  }))



class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'artist', 'album', 'length', 'cover']
        labels = {
            'name': 'Song Name',
            'length': 'Length (in seconds)',
            'artist': 'Artist Name',
            'album': 'Album Name'
        }
