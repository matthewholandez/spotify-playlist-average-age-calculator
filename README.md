# Spotify Playlist Average Age Calculator
Calculate the average age of all songs in a Spotify playlist.

## Installation
Clone the repository, navigate to the working directory and install dependencies with `pip install -r requirements.txt`.

Login to [https://developer.spotify.com/](https://developer.spotify.com/) and proceed to [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard).

Press 'Create App' and fill out the information. For redirect URI, simply use `http://localhost/` as a placeholder.

Then, copy your client ID and secret into `config.yaml.txt`. Afterwards, copy your playlist link from Spotify and get the playlist's ID. The ID will be located in the URL as follows:
```https://open.spotify.com/playlist/YOURIDHERE?si=....```

You may then copy your playlist ID into `config.yaml.txt`. **IMPORTANT: Ensure you then save `config.yaml.txt` as `config.yaml`.** If the file name is not changed, the program will not function!

Run the script with `python main.py`!