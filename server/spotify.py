import boto3
import spotipy

def pullSong(query):
    # return a song id, see if a related query is on spotify

    # if it is, return the song id
    if query() != query:
        return None
    # if not, return null
    else:
        return None

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