import fire

from controller import Controller


def start_playback(device=None, username=None):
    # Use kwarg for username so python-fire makes it a flag
    if not username:
        raise Exception("Please provide a username (--username)")

    ctrl = Controller(username=username)

    if device:
        ctrl.transfer(device_name=device)

    ctrl.play(device_name=device)


if __name__ == "__main__":
    fire.Fire(start_playback)
