import spotipy
import parseTreeer

parse = parseTreeer.parse

username = "masterjonis"
token = "BQC3Fbu99wvMr0ohbUQPpO5Ihx9Np4FxV336wmC8QEdM-lwJMjsiajNTK1sV3MJeITEUq5BLS_AC0aSgxoU3qaEHwEZsPGJgiF7AYv8DJmCZtXPKs0_7IT4QQCoPeaUf4VJ3hbgiq-vFxDWRYjbdsiKpFGMj8wkUzk6pqMPIuDnUlTSFjtJhcbDEZ8fS4S7HBKaw19drOJ0lDgA1S_2MDiPuzRSvSh1K1Y1saCF_nKCFObi_oQz7wIVjjLkGv6Id7REA"

sp = spotipy.Spotify(auth=token)
playlists = sp.user_playlists(username)["items"]

for playlist in playlists:
    print playlist['id']
    for trackItem in sp.user_playlist_tracks(username, playlist['id'])['items']:
        parse(trackItem)
    print
    
# parseTreeer.parse(playlists)
#sp.user_playlist_remove_all_occurrences_of_tracks(username, "3Uas2UPpSEOt2uzzwGZqAy", ["433"])