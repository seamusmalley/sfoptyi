import os
import sys
import json
import spotipy
import spotipy.util as util

from random import shuffle

from private import username, password

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

    print("Shuffling %s...\n" % playlists['items'][pl_ref]['name'])

    playlist_names = [playlist['name'] for playlist in playlists['items']]

    pl_name = playlists['items'][pl_ref]['name']
    shuffled_pl_name = 'sfoptyi-' + pl_name

    pl_id = playlists['items'][playlist_names.index(pl_name)]['uri'].split(':')[4]

    if shuffled_pl_name not in playlist_names:
        #TODO create playlist
        #TODO get shuffled_pl_id

    #TODO read tracks from original playlist
    #TODO shuffle tracks
    #TODO replace tracks in shuffled playlist with new shuffle of songs
