import os
import sys
import json
import spotipy
import webbrowser

import spotipy.util as util
from json.decoder import JSONDecodeError

from private import username, password

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

spotify = spotipy.Spotify(token)

playlists = spotify.user_playlists(username)
print("Playlists:")
i = 0
for playlist in playlists['items']:
    print('%d.\t%s' % (i, playlist['name']))
    i += 1

pl_id = int(input("\nPlaylist ID to shuffle: "))

print("Shuffling %s...\n" % playlists['items'][pl_id]['name'])
