import os


class PathManager:
    def __init__(self, path):
        self.path = path

    def create_by_path(self):
        print("Directory is not exists, creating...")
        os.makedirs(self.path)
        print("New directory created")
