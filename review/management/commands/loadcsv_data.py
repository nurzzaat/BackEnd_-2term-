import csv

from review.models import User, Artist, Album, Song, Playlist, PlaylistSong

# Open the CSV file and read the contents
with open('data.csv') as f:
    reader = csv.DictReader(f)

    # Loop over each row and create objects in the database
    for row in reader:
        if 'username' in row:
            User.objects.create(username=row['username'], password=row['password'], email=row['email'])
        elif 'name' in row and 'bio' in row:
            Artist.objects.create(name=row['name'], bio=row['bio'])
        elif 'name' in row and 'artist' in row and 'release_date' in row and 'genre' in row:
            Album.objects.create(name=row['name'], artist=Artist.objects.get(name=row['artist']),
                                  release_date=row['release_date'], genre=row['genre'])
        elif 'name' in row and 'artist' in row and 'album' in row and 'length' in row:
            Song.objects.create(name=row['name'], artist=Artist.objects.get(name=row['artist']),
                                 album=Album.objects.get(name=row['album']),
                                 length=row['length'])
        elif 'name' in row and 'user' in row:
            Playlist.objects.create(name=row['name'], user=User.objects.get(username=row['user']))
        elif 'playlist' in row and 'song' in row:
            playlist = Playlist.objects.get(name=row['playlist'])
            song = Song.objects.get(name=row['song'])
            PlaylistSong.objects.create(playlist=playlist, song=song)
