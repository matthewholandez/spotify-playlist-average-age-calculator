# Python 3.11.4
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
from yaml import Loader, load

# Get config
with open('config.yaml', 'r') as file:
    CONFIG = load(file, Loader=Loader)
    CLIENT_ID = CONFIG['client_id']
    CLIENT_SECRET = CONFIG['client_secret']
    PLAYLIST_ID = CONFIG['playlist_id']

# Authenticate
client_creds_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_creds_manager)

def calculate_age(release_date):
    birthday = datetime.strptime(release_date, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

def get_average_age(playlist):
    results = spotify.playlist_tracks(PLAYLIST_ID, fields='items.track.album.release_date,total')
    tracks = results['items']
    total_tracks = results['total']
    
    while len(tracks) < total_tracks:
        results = spotify.playlist_tracks(PLAYLIST_ID, fields='items.track.album.release_date,total', offset=len(tracks))
        tracks.extend(results['items'])
    
    total_age = 0

    for track in tracks:
        rd = track['track']['album']['release_date']
        total_age += calculate_age(rd)

    return total_age / total_tracks

avg = get_average_age(PLAYLIST_ID)
print(f'AVERAGE AGE: {avg:.2f} years')