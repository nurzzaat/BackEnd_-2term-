from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from django import forms

from .models import Song, User, Playlist


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=2)
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("Song", "Song"),
                                      ("Artist", "Artist")),
                                  widget=forms.Select(attrs={
                                      'class': 'my-select-class',
                                      'style': 'width: 250px; height: 30px; border: 1px solid #ccc; border-radius: '
                                               '4px; padding: 5px; font-size: 16px; box-shadow: 0 0 5px rgba(0, 0, 0,'
                                               ' 0.3);'
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

class PlayListForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['user', 'name', 'description']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'email-input',
        'style': 'width: 250px; height: 30px; border: 1px solid black; border-radius: 4px;'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-class',
                                                             'style': 'width: 250px; height: 30px; border: 1px solid black; border-radius: 4px;'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'my-class',
                                                                                   'style': 'width: 250px; height: 30px; border: 1px solid black; border-radius: 4px;'}))
    password_conf = forms.CharField(label="Password Confirmation",
                                    widget=forms.PasswordInput(attrs={'class': 'my-class',
                                                                      'style': 'width: 250px; height: 30px; border: 1px solid black; border-radius: 4px;'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_conf')
