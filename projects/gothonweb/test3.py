# -*- coding: utf-8 -*-
import spotipy
import parseTreeer
import re
import token

def main():
    parse = parseTreeer.parse
    
    username = "masterjonis"
    
    # token.token doesn't work in debug for some reason. so when debugging paste the token here and use this one instead.
    debug_token = "BQClISHE1VT5XjoNruRhOyieFqe_Ny0j1tTVrLGqBIBAXKyaJIYZNZ_7Np8dvAS3kMR7iX40yig01Cj-FhsGdOBzReZZcxdqGPWILs7zx5rLBypahv0QEzDUPLKN3ifEJSt72O6-YKACQQF-DhYPLUq60ZSp64E1cP-pnfTNH5RvyIrQ6tfMAU05xux4gEgLuLtB0pxE-sXQ-HET3VoZ0VlF7KS3jkFSgrKjDQadJFz1-qFRUD3azWNgmO4XsYMfyoq6"
   
    sp = spotipy.Spotify(auth=token.token)
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
                track_artists.append(str(artist["name"])) # (TODO: should be uri)
            
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
    
    duplicates = {}
    for track in tracks:
        duplicates_count = 0
        playlists = tracks[track]
        
        for playlist in playlists.itervalues():
            for track_in_playlist in playlist:
                duplicates_count += 1
        
        if duplicates_count > 1:
            duplicates[track] = tracks[track]
    
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
        
        if input == "exit":
            break
        elif not match:
            print "Wrong input, try again"
            continue
        
        track_nr = int(match.group(1)) - 1
        playlist_nr = int(match.group(2)) - 1
        keep = match.group(3)
        
        playlists = duplicates.values()[track_nr]
        playlist = playlists.keys()[playlist_nr]
        track_data = playlists.values()[playlist_nr]
    
        playlist_id = playlist[0]
        
        if keep == "none":
            track_uris = [get_uri(track_item) for track_item in track_data]
            sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, track_uris)
        else:
            tracks = []
            for i in range(1, len(track_data)):
                current_track_data = track_data[i]
                tracks.append({"uri" : current_track_data["uri"], "positions" : [current_track_data["position"]]})
            sp.user_playlist_remove_specific_occurrences_of_tracks(username, playlist_id, tracks)

def get_uris(track_data, keep):
    track_uri = track_item.values()[1]
    stripped_uri = re.match("spotify:track:(.*)", track_uri).group(1)  # (TODO) certain uri:s doesn't work
    return str(track_uri)

if __name__ == "__main__":
    main()