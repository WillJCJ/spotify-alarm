from alarm.alarm import (
    Controller,
    scope,
)


def test_controller(mocker):
    mocker.patch("spotipy.Spotify")
    mocked_prompt = mocker.patch("spotipy.util.prompt_for_user_token")

    mocked_prompt.return_value = "test_auth_token"

    sc = Controller("test_username")

    sc.pause()

    mocked_prompt.assert_called_once_with(username="test_username", scope=scope)
