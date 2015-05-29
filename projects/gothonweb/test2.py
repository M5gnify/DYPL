import spotipy
import parseTreeer

username = "masterjonis"
token = "BQCaiULf5xL6hlnuZinazfOQ_lizzfrsW8v0upy6dpp7aIUMkcb_lfkE84aquA1BbySe-cTuCU6ZKB0EguGiCDwjF72yrrH1hyKTMmbeZ0GQbndHDbO_uv633n68kDRMI6F1OdO1dlPoCY5VG6vPkAXL37uf1wlXJ_NkoZx6PKoGK5vQqpQH0nUwLoPbaO3IEpsKexiPLp8ceyuKJHvEK3-TK0vpVRIZv8VB9E8o4hHH0HlE2kyYbvs9Mhbzw6aBe42i"

sp = spotipy.Spotify(auth=token)
results = sp.user_playlists(username)

duplicates = {}

for playlist in results['items']:
    parseTreeer.parse(sp.user_playlist_tracks(username, playlist['id']))
    #print str(sp.user_playlist_tracks(username, playlist['id']))
    #for trackItem in sp.user_playlist_tracks("masterjonis", playlist['id'])['items']:
        #print trackItem["track"]
    print