import logging
import os

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

    def _get_device_id(self, device_name):
        device_id = None

        devices = self.sp.devices()["devices"]
        for device in devices:
            if device["name"] == device_name:
                device_id = device["id"]
                break
        if device_id:
            return device_id
        else:
            raise Exception(f"Could not find device with name {device_name}")

    def devices(self):
        """
        Get a list of all device names available to play on
        :return list: device names
        """
        return [device["name"] for device in self.sp.devices()["devices"]]

    def transfer(self, device_name, force_play=True):
        device_id = self._get_device_id(device_name)

        self.sp.transfer_playback(device_id=device_id, force_play=force_play)

    def play(self, device_name=None):
        device_id = None
        if device_name:
            device_id = self._get_device_id(device_name)

        self.sp.start_playback(device_id=device_id)
        logger.debug("playback resumed")

    def pause(self):
        self.sp.pause_playback()
        logger.debug("playback paused")
