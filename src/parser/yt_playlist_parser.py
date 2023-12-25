from pytube import Playlist
import requests
from src.dto.song_dto import SongDto
from src.interface import PlaylistParserInterface


class YtPlaylistParser(PlaylistParserInterface):
    def __init__(self, playlist_link=None, playlist_links=None):
        super().__init__(playlist_link, playlist_links)
        self.songs = []
        self.playlist_links = playlist_links

    def parse(self):
        playlist_links = self.__get_playlist() if self.playlist_link else self.playlist_links
        completed = 0
        for link in playlist_links:
            song_dto = self.get_song_dto(link)
            self.songs.append(song_dto)
            completed += 1
            print(f"Completed {completed}/{len(playlist_links)}")
            print()
        return self.songs

    # Getting a link to songs from a playlist
    def __get_playlist(self):
        urls = []
        playlist_urls = Playlist(self.playlist_link)
        for url in playlist_urls:
            urls.append(url)
        return urls

    def __get_link_payload(self, url):
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

    def get_song_dto(self, url):
        download_link_res = requests.post(
            "https://www.y2mate.com/mates/convertV2/index",
            headers=self.headers,
            data=self.__get_link_payload(url),
        )
        json_data = download_link_res.json()
        print(f"Link req status: {download_link_res.status_code}")
        print(f"Status: {download_link_res.json()['status']}")
        print(f"Song: {json_data['title']}")

        return SongDto(download_link=json_data["dlink"], title=json_data["title"])
