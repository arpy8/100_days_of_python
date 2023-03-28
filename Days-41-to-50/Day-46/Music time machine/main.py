import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

year = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
content = response.text
soup = BeautifulSoup(content, "html.parser")

selected_songs = soup.select(selector="li .o-chart-results-list__item")
formatted_songs = []
for song in selected_songs:
    try:
        song_title = song.find("h3").getText().strip()
        formatted_songs.append(song_title)
    except AttributeError:
        pass

print(formatted_songs)

# Spotify part of the code

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
URL_REDIRECT = "https://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []

for track in formatted_songs:
    search_results = sp.search(q=f"track: {track} year: {year.split('-')}", limit=10)
    try:
        uri = search_results['tracks']['items'][0]['uri']
        song_uris.append(uri)
        print(uri)
    except IndexError:
        pass
    except TypeError:
        pass

check_create = input('Would you like to create a playlist with these songs? Type y or n: ')

if check_create == 'y':
    billboard_playlist = sp.user_playlist_create(user=user_id, name=f"{year} Top Hits", public=False,
                                                 collaborative=False, description=f"Top Billboard 100 for {year}.")
    sp.playlist_add_items(playlist_id=billboard_playlist['id'], items=song_uris, position=None)
    print('playlist successfully created!')
else:
    print("No worries.")