# -*- coding: utf-8 -*-
import spotipy
import parseTreeer
import re
import token
import sys

token = "BQCkDgLoA4nbvF5HkwvSdx2--x3-KNi65jB8XqyqNfK2_VC_V9WCZ8Qcx_LUX-6f6kGDl3AvLvfM0KdzNS-xlebUQfeUrdVb3Fo9jz7f2u4Cj-sreBQq5z2U1CC40WnOoOQrTwGs0bApdUOIdveYCzHkMBvQcxqKoS2X6TDoifY4eFOi3CleJcrrzBwXTcZ4035OcnxCNL2P2vdClExUkWwB_PZgOS3Ow-eGYcDsRKFgFQWmz17-GdnWJYiBez6DX1GP"
username = "masterjonis"
sp = spotipy.Spotify(auth=token)

def main():
    while True:
        tracks = get_user_tracks()
        duplicates = get_duplicates(tracks)
        
        if len(duplicates) == 0:
            print "No duplicates, congratulations! You won! Bye bye"
            sys.exit(0)
        
        print_duplicates(duplicates)
        
        input = raw_input("Which song(s) do you want to remove from which playlist? Type the number of the song followed by the number of the playlist separated by a dot, and after that either 'one' to keep one instance of the track or 'none' to remove all instances, e.g. '1.1 none', or '3.4 one'. Type 'exit' to exit the program:\n").strip()
        match = re.match("(\d+)\.(\d+) (one|none)", input)
        
        if input == "exit":
            break
        elif not match:
            print "Wrong input, try again"
            continue
        
        try:
            remove_duplicates(duplicates, match)
        except IndexError:
            print "Non-existing track or playlist number"
            continue
        
        print "Duplicates removed."

def get_user_tracks():
    user_playlists = sp.user_playlists(username)["items"]
    tracks = {}
    
    for playlist in user_playlists:
        playlist_tracks = sp.user_playlist_tracks(username, playlist["id"])["items"]
        
        for index, track_item in list(enumerate(playlist_tracks)):
            # the spotipy API can't handle local track uri:s
            if track_item["is_local"]:  
                continue
            
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
        
    return tracks

def get_duplicates(tracks):
    duplicates = {}
    for track in tracks:
        duplicates_count = 0
        playlists = tracks[track]
        
        for playlist in playlists.itervalues():
            for track_in_playlist in playlist:
                duplicates_count += 1
        
        if duplicates_count > 1:
            duplicates[track] = tracks[track]
    
    return duplicates
    
def print_duplicates(duplicates):
    track_nr = 1        # to be used in the output to let the user specify which song to remove 
    playlist_nr = 1     # to be used in the output to let the user specify which playlist to remove
    
    print "Duplicates:"
    for track in duplicates:
        playlists = duplicates[track]
        duplicates_count = 0
        
        for playlist in playlists.itervalues():
            for track_in_playlist in playlist:
                duplicates_count += 1
                
        print "{0} {1} by {2} (Total occurences: {3})".format(track_nr, track[0], str(track[1]), duplicates_count)
        
        for playlist in playlists:
            message = "{0} (count: {1})".format(playlist[1], len(playlists[playlist]))
            print "   {0} {1}".format(playlist_nr, message)
            playlist_nr += 1
            
        print
        playlist_nr = 1
        track_nr += 1

def remove_duplicates(duplicates, user_input):
    track_nr = int(user_input.group(1)) - 1
    playlist_nr = int(user_input.group(2)) - 1
    keep = user_input.group(3)      # either "none" for keeping none of the track occurences, or "one" for keeping one occurence
    
    playlists = duplicates.values()[track_nr]
    playlist = playlists.keys()[playlist_nr]
    track_data = playlists.values()[playlist_nr]

    playlist_id = playlist[0]
    
    if keep == "none":
        track_uris = [str(track_item.values()[1]) for track_item in track_data]
        sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, track_uris)
    else:
        tracks = []
        for i in range(1, len(track_data)):
            current_track_data = track_data[i]
            tracks.append({"uri" : current_track_data["uri"], "positions" : [current_track_data["position"]]})
        sp.user_playlist_remove_specific_occurrences_of_tracks(username, playlist_id, tracks)

if __name__ == "__main__":
    main()