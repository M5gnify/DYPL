# -*- coding: utf-8 -*-
import spotipy
import parseTreeer
import re

username = "masterjonis"
token = "BQC3Fbu99wvMr0ohbUQPpO5Ihx9Np4FxV336wmC8QEdM-lwJMjsiajNTK1sV3MJeITEUq5BLS_AC0aSgxoU3qaEHwEZsPGJgiF7AYv8DJmCZtXPKs0_7IT4QQCoPeaUf4VJ3hbgiq-vFxDWRYjbdsiKpFGMj8wkUzk6pqMPIuDnUlTSFjtJhcbDEZ8fS4S7HBKaw19drOJ0lDgA1S_2MDiPuzRSvSh1K1Y1saCF_nKCFObi_oQz7wIVjjLkGv6Id7REA"

sp = spotipy.Spotify(auth=token)
playlists = sp.user_playlists(username)["items"]

tracks = {}

for playlist in playlists:
    playlist_tracks = sp.user_playlist_tracks(username, playlist["id"])["items"]
    
    for index, track_item in list(enumerate(playlist_tracks)):
        track = track_item["track"]
        track_name = track["name"]
        track_uri = track["uri"]
        
        track_artists = []
        for artist in track["artists"]:
            track_artists.append(str(artist["name"]))
        
        track_key = (str(track_name), tuple(track_artists))
        playlist_key = (playlist["id"], playlist["name"])
        track_data = {"uri" : track_uri, "position" : index}
        
        if tracks.has_key(track_key):
            track_playlists = tracks[track_key]
            
            if track_playlists.has_key(playlist_key):
                track_playlists[playlist_key].append(track_data)
            else:
                track_playlists[playlist_key] = [track_data]
        else:
            tracks[track_key] = {playlist_key : [track_data]}

#parseTreeer.parse(tracks)

duplicates = {}
for track in tracks:
        duplicates_count = 0
        playlists = tracks[track]
        
        for playlist in playlists.itervalues():
            for track_in_playlist in playlist:
                duplicates_count += 1
        
        if duplicates_count > 1:
            duplicates[track] = tracks[track]

#parseTreeer.parse(duplicates)

while True:
    track_nr = 1        # to be used in the output to let the user specify which song to remove 
    playlist_nr = 1     # to be used in the output to let the user specify which playlist to remove
    
    for track in duplicates:
        playlists = duplicates[track]
        duplicates_count = 0
        
        for playlist in playlists.itervalues():
            for track_in_playlist in playlist:
                duplicates_count += 1
                
        print "{0} {1} by {2} (Total duplicates: {3})".format(track_nr, track[0], track[1], duplicates_count)
        
        for playlist in playlists:
            message = "{0} (count: {1})".format(playlist[1], len(playlists[playlist]))
            print "   {0} {1}".format(playlist_nr, message)
            playlist_nr += 1
            
        print
        playlist_nr = 1
        track_nr += 1
    
    input = raw_input("Which song(s) do you want to remove from which playlist? Type the number of the song followed by the number of the playlist separated by a dot, and after that either 'one' to keep one instance of the track or 'none' to remove all instances, e.g. 1.1 none:\n").strip()
    match = re.match("(\d)\.(\d) (one|none)", input)
    
    if input == "exit" or not match:
        break
    
    track_nr = int(match.group(1)) - 1
    playlist_nr = int(match.group(2)) - 1
    
    track = duplicates.values()[track_nr]
    playlist = track.keys()[playlist_nr]
    track_data = track.values()[0][playlist_nr]

    playlist_id = playlist[0]
    track_uri = track_data["uri"]
    position = track_data["position"]
    
    match2 = re.match("spotify:track:(.*)", track_uri)
    if match.group(3) == "one":
        # TODO: fixa denna
        sp.user_playlist_remove_specific_occurrences_of_tracks(username, playlist, tracks)
    else:
        sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, [match2.group(1)])