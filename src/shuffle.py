import os
import sys
import json
import spotipy
import spotipy.util as util
import random

from private import username

try:
    token = util.prompt_for_user_token(username, 'playlist-modify')
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, 'playlist-modify')

if token:
    spotify = spotipy.Spotify(auth=token)
    spotify.trace = False

    playlists = spotify.user_playlists(username)
    print("Playlists:")
    i = 0
    for playlist in playlists['items']:
        print('%d.\t%s' % (i, playlist['name']))
        i += 1

    pl_ref = int(input("\nPlaylist ID to shuffle: "))

    print("Shuffling %s..." % playlists['items'][pl_ref]['name'])

    playlist_names = [playlist['name'] for playlist in playlists['items']]

    pl_name = playlists['items'][pl_ref]['name']
    if pl_name.startswith('sfoptyi'):
        shuffled_pl_name = pl_name
    else:
        shuffled_pl_name = 'sfoptyi-' + pl_name

    if shuffled_pl_name not in playlist_names:
        spotify.user_playlist_create(username, shuffled_pl_name, public=True)
        playlists = spotify.user_playlists(username)
        playlist_names = [playlist['name'] for playlist in playlists['items']]

    pl_id = playlists['items'][playlist_names.index(pl_name)]['uri'].split(':')[4]
    shuffled_pl_id = playlists['items'][playlist_names.index(shuffled_pl_name)]['uri'].split(':')[4]

    pl_tracks = [track['track']['id'] for track in spotify.user_playlist(username, pl_id)['tracks']['items']]
    random.shuffle(pl_tracks)

    spotify.user_playlist_replace_tracks(username, shuffled_pl_id, pl_tracks)

    print("Enjoy!")
