import json
import re
import requests
import spotipy
from config import CLIENT_SECRET, CLIENT_ID, REDIRECT_URI
from src.spotify_links_extractor import SpotifyLinksExtractor

from src.interface.playlist_parser_interface import PlaylistParserInterface


class SpotifyLinksParser(PlaylistParserInterface):
    def __init__(self, playlist_link: str, spotify_link_extractor: SpotifyLinksExtractor):
        super().__init__(playlist_link)
        self.oauth = spotipy.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
        self.token = self.oauth.get_access_token()["access_token"]
        self.spot = spotipy.Spotify(auth=self.token)
        self.links = []
        self.completed = 0
        self.spotify_link_extractor = spotify_link_extractor

    def parse(self):
        spotify_links = self.spotify_link_extractor.extract()
        for song in spotify_links["items"]:
            link = self.get_song_link(song["track"] if "track" in song else song, len(spotify_links["items"]))
            self.links.append(link)
        return self.links

    def get_song_link(self, song, songs_length: int, ):
        try:

            name = song["name"]
            artist_name = song["artists"][0]["name"]
            search_name = f"{name} - {artist_name}"
            html = requests.get(f"https://www.youtube.com/results?search_query={search_name}", headers=self.headers)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.text)
            global video_id
            if video_ids[0] != video_ids[1]:
                video_id = video_ids[1]
            else:
                video_id = video_ids[0]

            song_link = f"https://www.youtube.com/watch?v={video_id}"
            self.completed += 1
            print(f"Parsed link for: {search_name} {self.completed}/{songs_length}")
            return song_link
        except Exception as e:
            print(e)
