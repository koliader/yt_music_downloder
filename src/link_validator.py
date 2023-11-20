import sys
from urllib.parse import urlparse

import validators


class LinkValidator:
    def __init__(self, link):
        self.link = link

    def validate(self):
        validation = validators.url(self.link)
        # Check is link
        if validation:
            self.check_platform()
        else:
            print("Link is not valid")
            sys.exit(0)

    def check_platform(self):
        domain = urlparse(self.link).netloc
        # Check is link from YouTube or YouTube Music
        if domain == "music.youtube.com" or domain == "www.youtube.com":
            pass
        else:
            print("Link is not valid")
            print('Enter playlist link from "YouTube Music" or "YouTube"')
            sys.exit(0)
