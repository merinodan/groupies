import boto3
import botocore
import spotipy
import os
import spotipy.util as util
import json
import datetime

scope = 'user-read-private playlist-modify-public'
username = '1225094990'
token = util.prompt_for_user_token(username, scope)
sp = spotipy.Spotify(auth=token)

class Song(object): # define Song object
    def __init__(self, song_name, song_id):
        self.song_name = ""
        self.song_id = ""

def songify(titles, playlist):   # 'songify' all the titles and add them to the playlist
    limit = 10
    i = 0
    for title in titles:
        NewSong = pullSong(title)

        if NewSong is not None:
            song_id = NewSong[1]
            sp.user_playlist_add_tracks(username, playlist, [song_id]) # add the song to the playlist
            print(('added ' + NewSong[0] + ' to playlist ' + playlist))
            i += 1

        if i >= limit:  # stop at the limit, so you don't add songs ad infinitum
            break

def pullSong(title):
    # see if a related query is on spotify, if so, return a song id
    data = sp.search(q=title, limit=1, type='track')
    
    try:
        song_name = data["tracks"]["items"][0]["name"]
        song_id = data["tracks"]["items"][0]["id"]
        
        return (song_name, song_id)
    except:
        return None
    
def createPlaylist(query):
    # create a new playlist
    currentDT = datetime.datetime.now()

    playlist_name = query + " - groupies - " + currentDT.strftime("%m-%d-%Y")

    playlist_id = sp.user_playlist_create(username, playlist_name, public=True)["id"]

    # return the newly created playlist's id
    return playlist_id

def songScramble(playlist_name):
    # scramble the songs in the playlist

    return playlist_name