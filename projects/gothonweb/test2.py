import spotipy

username = "masterjonis"
token = "BQDA-40ApEBxiGhnrzJrJ7kUKaOi0xG3LEYd3ZlyO2NeN70YaBk8U-FEGaFIQqx_lQtIEINxJoT-hbres9DbwQ8IKTww0u7yV2DGUtNQOmT7Goz8iD7EfokYpAfvwv8NuN675Nzj1Nz34DVULm7eB549Y15RxKRcZeybyHgy7-e76DFGNPFP7AGYpvIgvTej_Ue-CT-4B399YIBvvt9CbS9D85EvvZGATygGpU1KZaJnzflVcn5IYqVnobwM"

sp = spotipy.Spotify(auth=token)
results = sp.user_playlists(username)

duplicates = {}

for playlist in results['items']:
    print playlist["name"], ":"
    for trackItem in sp.user_playlist_tracks("masterjonis", playlist['id'])['items']:
        print trackItem["track"]
    print