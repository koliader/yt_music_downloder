from pytube import Playlist


class ParsePlaylist:
    def __init__(self, link):
        self.link = link
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }

    def parse(self):
        return self.get_playlist()

    # Getting a link to songs from a playlist
    def get_playlist(self):
        urls = []
        playlist_urls = Playlist(self.link)
        for url in playlist_urls:
            urls.append(url)
        return urls
