import os
from .path_manager import PathManager


class PathValidator:
    def __init__(self, path):
        self.path = path
        self.path_manager = PathManager(path)

    def validate(self):
        is_exists = os.path.exists(self.path)
        if not is_exists:
            print("Directory is not exists, creating...")
            self.path_manager.create_by_path()
            print("New directory created")
