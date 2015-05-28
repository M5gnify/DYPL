import sys
import spotipy
import spotipy.util as util

token = "BQA2mIIhjSigxdujUfVFHXySVeIFTTtRqIzjUD2NRTvMCDU7UdQQJslm3WtLZd_WsTTfZfSm983vIEPKRhaS3FD67QJoubBc5QeEiiNV0PM3bj1fwPfSGNLVSzgAj8lOyrSigog2fo8sm1HUrc9dwC7QUTFxjwlK4foeOUFvNh7B5qAAhcBQlCpGrpU1FD8zjv-dvR1UDE5lRdU2fFGKR4XP4K1P9HsGi1eannyhDRVkL1KmDYWgJvUvKx8Q"

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.user_playlists("masterjonis")
    for playlist in results['items']:
        #print sp.user_playlist_tracks("masterjonis", playlist["id"])
        print playlist["name"], ":"
        for track in sp.user_playlist_tracks("masterjonis", playlist['id'])['items']:
            print track["track"]
        print "\n"
else:
    print "Can't get token"
