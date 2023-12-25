import json

import spotipy
from config import CLIENT_SECRET, CLIENT_ID, REDIRECT_URI


class SpotifyLinksExtractor:
    def __init__(self, link: str):
        self.oauth = spotipy.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
        self.token = self.oauth.get_access_token()["access_token"]
        self.spot = spotipy.Spotify(auth=self.token)
        self.link = link

    def extract(self):
        resource = self.link.split("/")[3]
        resource_id = self.link.split("/")[-1][:22]
        if resource == "album":
            return self.extract_from_album()
        elif resource == "playlist":
            return self.extract_from_playlist(resource_id)

    def extract_from_playlist(self, playlist_id: str):
        playlist = self.spot.playlist_items(playlist_id)
        return playlist

    def extract_from_album(self):
        album = self.spot.album_tracks(self.link)
        return album
