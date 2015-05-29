import spotipy

username = "masterjonis"
token = "BQBesH0O5hVc-MFctTqtUuhyWG4bR1HG8TQTKtyLqGuJ2iEGyYKhBDOT7XF9fBScS_CtWlfzZKapeBTFclzVATby262F-9v3YgCwMHEMonBdnm2iqz16nv4Pf1e6tHx8DY2pHwDDKxba63PlRgmF8Ww2qaP3i_KkpkhGr_pPclNVZjBXqAQknovAfjxJhdIm7O9ndDsLtd3_S-E6ygBKzcnVLQUdjiDSeF0ijoBYftlom2kKs3-lDQkqV0n5BTdoV-oI"

sp = spotipy.Spotify(auth=token)
results = sp.user_playlists(username)

duplicates = {}

for playlist in results['items']:
    print str(sp.user_playlist_tracks(username, playlist['id']))
    #for trackItem in sp.user_playlist_tracks("masterjonis", playlist['id'])['items']:
        #print trackItem["track"]
    print