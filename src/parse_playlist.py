from pytube import Playlist
import requests
from .dto.song_dto import SongDto
from .saver import Saver


class ParsePlaylist:
    def __init__(self, playlist_link):
        self.playlist_link = playlist_link
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
        self.songs = []

    def parse(self):
        playlist_links = self.__get_playlist()
        for link in playlist_links:
            song_dto = self.__get_song_data(link)
            self.songs.append(song_dto)

        return self.songs

    # Getting a link to songs from a playlist
    def __get_playlist(self):
        urls = []
        playlist_urls = Playlist(self.playlist_link)
        for url in playlist_urls:
            urls.append(url)
        return urls

    def __get_key(self, url):
        key_payload = {"k_query": url, "k_page": "home", "hl": "en", "q_auto": 1}
        response = requests.post(
            "https://www.y2mate.com/mates/analyzeV2/ajax",
            data=key_payload,
            headers=self.headers,
        )
        print(f"Key req status: {response.status_code}")
        json_data = response.json()
        link_payload = {
            "vid": json_data["vid"],
            "k": json_data["links"]["mp3"]["mp3128"]["k"]
        }
        return link_payload

    def __get_song_data(self, url):
        download_link_res = requests.post(
            "https://www.y2mate.com/mates/convertV2/index",
            headers=self.headers,
            data=self.__get_key(url),
        )
        json_data = download_link_res.json()
        print(f"Link req status: {download_link_res.status_code}")
        print(f"Status: {download_link_res.json()['status']}")
        print(f"Song: {json_data['title']}")
        print()
        return SongDto(download_link=json_data["dlink"], title=json_data["title"])
