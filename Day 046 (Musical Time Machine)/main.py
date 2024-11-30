import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

CLIENT_ID = "7375932d8da14e229e5869c105090fe9"
CLIENT_SECRET = "83ac1ad780444adabca4f106e529a70f"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/#"

response = requests.get(url=URL)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
all_songs = soup.select(selector="li ul li h3")
list_of_songs = [song.getText().strip() for song in all_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="isaacisamartin"
                                               ))

user_id = sp.current_user()['id']
song_uris = []
year = date.split("-")[0]

for song in list_of_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pprint(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

my_playlist = sp.user_playlist_create(user=user_id,public=False,name="Hot 100 Time Machine",description="Top Tracks from back in the Days")

x = sp.playlist(playlist_id=my_playlist)
print(x)
#
# sp.playlist_add_items(playlist_id="", items= ,position=None)
# print(song_uris)

#need to understand how to get spotify playist_id