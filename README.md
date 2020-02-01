# Spotify Alarm Clock

Uses the Spotify API to resume playback on a specific device.

Can be scheduled to run so you can use it as an alarm clock.

## Environment Variables

The following variables are required to connect to the Spotify API

- `SPOTIPY_REDIRECT_URI`
    Example: `http://callback`
- `SPOTIPY_CLIENT_ID`
- `SPOTIPY_CLIENT_SECRET`

## `crontab`

If you want to schedule it with cron, you can use the following `crontab` entry:

```text
0 6 * * * . ~/.spotipy_creds.sh && cd /path/to/spotify-alarm && venv/python alarm/alarm.py --username MY_USERNAME
```

Notice it sources the Spotify credentials first so the script can run.
You will need to set up a file like this or just hardcode the credentials in the crontab.

Example credentials file:

```sh
export SPOTIPY_REDIRECT_URI=http://callback
export SPOTIPY_CLIENT_ID=xxx
export SPOTIPY_CLIENT_SECRET=xxx
```

## TODO

- Add setup to get a .cache-<username> file locally _before_ running.
- Check for a cache file with the right name and exit if it doesn't exist.
- Choose an optional playlist or artist to play instead of just resuming playback.
- Docstrings on all the functions. (Thanks flake8-docstrings...)
- Make the setup clearer (callback url etc)
