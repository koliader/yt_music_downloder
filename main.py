from src.parser.spotify_links_parser import SpotifyLinksParser
from src.parser.yt_playlist_parser import YtPlaylistParser
from src.parser.argument_parser import ArgumentParer
from src.validator.link_validator import LinkValidator
from src.validator.path_validator import PathValidator
from src.saver import Saver
from src.path_manager import PathManager
from src.spotify_links_extractor import SpotifyLinksExtractor


def main():
    # Get data from user
    argument_parser = ArgumentParer()
    user_data_dto = argument_parser.get_args()

    # Validate link
    link_validator = LinkValidator(user_data_dto.link)
    link_validator.validate()

    # Validate path
    path_validator = PathValidator(user_data_dto.path)
    folder_is_exists = path_validator.validate()

    # Create path or not
    path_manager = PathManager(user_data_dto.path)
    if not folder_is_exists:
        path_manager.create_by_path()
    global songs
    # Create link parser from playlist
    if "spotify" in user_data_dto.link:
        spotify_link_extractor = SpotifyLinksExtractor(user_data_dto.link)
        parser = SpotifyLinksParser(user_data_dto.link, spotify_link_extractor)
        yt_links = parser.parse()
        yt_parser = YtPlaylistParser(playlist_links=yt_links)
        songs = yt_parser.parse()
    else:
        yt_parser = YtPlaylistParser(playlist_link=user_data_dto.link)
        songs = yt_parser.parse()
    # # Save songs
    saver = Saver(songs, user_data_dto.path)
    saver.download_songs()
    print("All is saved successfully!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
