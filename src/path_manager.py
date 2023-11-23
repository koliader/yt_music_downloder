import os


class PathManager:
    def __init__(self, path):
        self.path = path

    def create_by_path(self):
        os.makedirs(self.path)
