import os
import requests
from src.get_link import GetLink
from src.parse_playlist import ParsePlaylist
from src.user_data_disp import UserDataDispatcher
from src.validator import Validator

user_data_disp = UserDataDispatcher()
user_data = user_data_disp.get_user_data()
validator = Validator(user_data)
validator.validate()
link_disp = GetLink()
parser = ParsePlaylist(user_data["link"])
urls = parser.parse()
downloaded = 0
for url in urls:
    res = link_disp.get_link(url)
    print(f'Saving "{res["title"]}" ...')
    fil_path = os.path.join(
        user_data["directory"].replace("/", "//"), f"{res['title']}.mp3"
    )
    song = requests.get(res["link"])
    with open(fil_path, "wb") as f:
        f.write(song.content)
    downloaded += 1
    print(f'"{res["title"]}" saved')
    print(f"Downloaded {downloaded}/{len(urls)}")
    print()

print("All is saved successfully!")
