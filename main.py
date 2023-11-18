import os
import re
import requests
from src.get_link import GetLink
from src.parse_playlist import ParsePlaylist
from src.user_data_disp import UserDataDispatcher
from src.validator import Validator


def main():
    # Get data from user
    user_data_disp = UserDataDispatcher()
    user_data = user_data_disp.get_user_data()

    # Validate user data
    validator = Validator(user_data)
    validator.validate()
    
    # Create link dispatcher
    link_disp = GetLink()

    # Create url parser from playlist
    parser = ParsePlaylist(user_data["link"])
    urls = parser.parse()
    downloaded = 0

    # Download each song from playlist
    for url in urls:
        # Get download link
        res = link_disp.get_link(url)
        print(f'Saving "{res["title"]}" ...')

        song_name = f'{res["title"]}.mp3'
        song_name = re.sub(r'[\\/*?:"<>|]', "_", song_name)

        fil_path = os.path.join(
            user_data["directory"], song_name)

        # Get song
        song = requests.get(res["link"])
        # Save it
        with open(fil_path, "wb") as f:
            f.write(song.content)
        downloaded += 1
        print(f'"{res["title"]}" saved')
        print(f"Downloaded {downloaded}/{len(urls)}")
        print()

    print("All is saved successfully!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
