class PlaylistParserInterface:
    def __init__(self, playlist_link=None, playlist_links=None):
        self.playlist_link = playlist_link
        self.playlist_links = playlist_links
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }

    def parse(self):
        pass

    def get_playlist(self):
        pass
