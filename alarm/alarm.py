import logging
import os

import fire
import spotipy
import spotipy.util as util

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
logger.addHandler(handler)

scope = """
playlist-read-private
playlist-read-collaborative
user-library-read
user-modify-playback-state
user-read-currently-playing
user-read-playback-state
"""


def get_auth_token(username):
    token = util.prompt_for_user_token(username=username, scope=scope)
    if not token:
        raise Exception(f"Can't get token for {username}")
    return token


class Controller:
    def __init__(self, username):
        token = get_auth_token(username)
        self.sp = spotipy.Spotify(auth=token)

    def play(self):
        self.sp.start_playback()
        logger.debug("playback resumed")

    def pause(self):
        self.sp.pause_playback()
        logger.debug("playback paused")


if __name__ == '__main__':
    fire.Fire(Controller)
