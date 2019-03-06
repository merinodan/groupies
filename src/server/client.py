import wiki as w
import spotify as sp

def createGroupie(query):
    # create a groupie
    # 1. search for a query
    # 2. pull links from wikipedia
    # 3. pull songs from spotify from links
    # 4. create playlist
    # 5. add songs to playlist
    # 6. optional: song scramble
    # 7. return and display playlist

    links = w.getTitles(query)
    playlist = sp.createPlaylist(query)
    sp.songify(links, playlist)

    return ('groupie created for ' + query)

def displayGroupie(groupie):
    # display the new playlist

    list = groupie

    return list