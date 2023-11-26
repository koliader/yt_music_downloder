import argparse
from src.dto.user_data_dto import UserDataDto


class ArgumentParer:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = ""

    def get_args(self):
        self.__set_args()
        return self.__save_args()

    def __set_args(self):
        self.parser.add_argument("-l", "--link", help="Link to playlist for parse")
        self.parser.add_argument("-p", "--path", help="Path to save songs")

    def __save_args(self):
        args = self.parser.parse_args()
        return UserDataDto(link=args.link, path=args.path)
