import os


class PathValidator:
    def __init__(self, path):
        self.path = path

    def validate(self):
        is_exists = os.path.exists(self.path)
        if not is_exists:
            print("Directory is not exists, creating...")
            os.makedirs(self.path)
            print("New directory created")
