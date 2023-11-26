import os


class PathValidator:
    def __init__(self, path):
        self.path = path

    def validate(self) -> bool:
        is_exists = os.path.exists(self.path)
        if not is_exists:
            return False
        else:
            return True
