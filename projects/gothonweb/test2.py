import spotipy
import parseTreeer
import token

parse = parseTreeer.parse

username = "masterjonis"

sp = spotipy.Spotify(auth=token.token)
playlists = sp.user_playlists(username)["items"]
parse( playlists)
# for playlist in playlists:
#     print playlist['name']
#     for trackItem in sp.user_playlist_tracks(username, playlist['id'])['items']:
#         parse(trackItem)
#     print
    
# parseTreeer.parse(playlists)
#sp.user_playlist_remove_all_occurrences_of_tracks(username, "5wEqYYiT6roVtkdF75bMvM", ["2HbVINmehEbPmjlcueXEJJ", "40Gxnw5Vc8hnhGFknXHe3R"])