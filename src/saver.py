import os
import re
import requests


class Saver:
    def __init__(self, songs, path):
        self.path = path
        self.downloaded = 0
        self.songs = songs

    def download_songs(self):
        for song in self.songs:
            print(f'Saving "{song.title}" ...')
            # Normalize path
            file_path = self.__normalize_path(song)

            # Save song
            song_res = requests.get(song.download_link)
            with open(file_path, "wb") as f:
                f.write(song_res.content)

            self.downloaded += 1
            print(f'"{song.title}" saved')
            print(f"Downloaded {self.downloaded}/{len(self.songs)}")
            print()

    def __normalize_path(self, song):
        normalized_song_name = re.sub(r'[\\/*?:"<>|]', "_", song.title)
        fil_path = os.path.join(
            self.path, f"{normalized_song_name}.mp3")
        return fil_path
