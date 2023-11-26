from src.parsers.playlist_parser import PlaylistParser
from src.parsers.argument_parser import ArgumentParer
from src.validators.link_validator import LinkValidator
from src.validators.path_validator import PathValidator
from src.saver import Saver
from src.path_manager import PathManager


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

    # Create link parser from playlist
    parser = PlaylistParser(user_data_dto.link)
    songs = parser.parse()

    # Save songs
    saver = Saver(songs, user_data_dto.path)
    saver.download_songs()
    print("All is saved successfully!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
