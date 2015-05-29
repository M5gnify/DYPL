# -*- coding: utf-8 -*-
import spotipy

username = "masterjonis"
token = "BQCKwvTlCWz02PLDXvMPnqWzblHmegE5jYh1XtKYPumU4YNtu0eCR4bIxbQo4uUXIAx3wk85ujxpwBhcVvN0MLaQikOTf_9N86ADqbl8sxp0XSy8JyTIDCDet-LZPqvhW7vsSAYdvwR9ti3J3JdOojmsehrdssrgS0NSisfyPtbwDGvDaMfx9GeXPIMXJvSXelQkqCpXOInyW0mHvAKEOOenzmOhiIKhk05yUrrkU7YCBDKxvhRSheGtKQwCbok5rsXf"

sp = spotipy.Spotify(auth=token)
results = sp.user_playlists(username)

duplicates = {}

for playlist in results['items']:
	playlist_name = str(playlist['name'])
	for trackItem in sp.user_playlist_tracks(username, 	playlist['id'])['items']:
		#print trackItem["track"]
		key = (str(trackItem["track"]["name"]), str( trackItem["track"]["artists"][0]["name"]))
		if duplicates.has_key(key):
			trackPlaylists = duplicates[key]
			if trackPlaylists.has_key(playlist_name): 
				duplicates[key][playlist_name] += 1
			else:
				duplicates[key][playlist_name] = 1
		else:
			duplicates[key] = {playlist_name : 1}
while True:
	i = 1
	j = 1

	for track in duplicates:
		totalCount = 0
		for count in duplicates[track].itervalues():
			totalCount += count
		if not totalCount > 1:
			continue
		print i, track[0], "by", track[1], "Total count:", totalCount
		for playlist, count in duplicates[track].iteritems():
			if len(duplicates[track]) > 1 or duplicates[track][playlist] > 1:
				print '  ', j, playlist, "count:", count, "(Remove all but one)"
				j += 1
				print '  ', j, playlist, "count:", count, "(Remove all)"
				j += 1
		print
		j = 1
		i += 1
	input = raw_input( "Which song(s) do you want to remove from which playlist? Type the number of the song followed by the number of the playlist separated by a dot, e.g. 1.1 1.2:")
	
	if input.strip == "exit":
		break
	if input.strip ==
