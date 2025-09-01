import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "7375932d8da14e229e5869c105090fe9"
CLIENT_SECRET = "83ac1ad780444adabca4f106e529a70f"

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
# url = "https://www.billboard.com/charts/hot-100/" + date

# response = requests.get(url=url,headers=header)
# music_web_page = response.text

# soup = BeautifulSoup(music_web_page,"html.parser")
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="isaacisamartin", 
    )
)
user_id = sp.current_user()["id"]
