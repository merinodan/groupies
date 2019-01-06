import boto3
import botocore
import spotipy
import os
import spotipy.util as util
import json

scope = 'user-read-private user-read-playback-state user-modify-playback-state user-read-currently-playing'
username = '1225094990'
token = util.prompt_for_user_token(username, scope)
sp = spotipy.Spotify(auth=token)

def pullSongs(links):
    # see if a related query is on spotify, if so, return a song id
    songlist = []
    urilist = []

    for link in links:  # for every song, search for it and keep track of its name and UID
        data = sp.search(q=link, limit=1, type='track')

        try:
            songlist.append(data["tracks"]["items"][0]["name"])
            urilist.append(data["tracks"]["items"][0]["uri"])
        except:
            songlist.append("No song found for " + link)

    # print(urilist)

    return songlist

def createPlaylist(playlist_name):
    # create a new playlist

    # sp.user_playlist_create(username, playlist_name, playlist_description)

    return 'playlist created'

def addToPlaylist(song_id, playlist_name):
    # adds the song to a playlist

    # sp.user_playlist_add_tracks(username, playlist_id, track_ids)

    return 'song added'

def songScramble(playlist_name):
    # scramble the songs in the playlist

    return playlist_name