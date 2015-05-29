# -*- coding: utf-8 -*-
import spotipy

username = "masterjonis"
token = "BQBMqwyk5d9G-Qzhf2zIjqfGpYCsPTJjNvMZ4aCIwRx811F4_eu91s09H6vHxaMCBoBJAHXpbPLZzf8UJUy24ZS320ZTQ-kJO-qrFL6zPhCMR-pbNEnkGNHP4Cg6124u_gSq949fIMxv6AEnHouX4VYC-1Q3KVbkzoYyjQaBIaaSG5VoPrLt13TjxNJttAJnFOGDA0VvFYhwZiTIkRMEIhUTe81rPXam-yemH0SbWQuYwPMVfZ8sXydfNL97UsbgOPvA"

sp = spotipy.Spotify(auth=token)
results = sp.user_playlists(username)

songs = {}

for index, playlist in list(enumerate(results['items'])):
	playlist_name = str(playlist['name'])
	for trackItem in sp.user_playlist_tracks(username, playlist['id'])['items']:
		#print trackItem["track"]
		key = (str(trackItem["track"]["name"]), str( trackItem["track"]["artists"][0]["name"]))
		if songs.has_key(key):
			trackPlaylists = songs[key]['playlists']
			if trackPlaylists.has_key(playlist_name): 
				songs[key]['playlists'][playlist_name].append(index)
			else:
				songs[key]['playlists'][playlist_name] = [index]
		else:
			songs[key] = {'playlists' : {playlist_name : [index]}, 'uri' : trackItem['track']['uri']}
duplicates = {}
while True:
	i = 1
	j = 1

	for track in songs:
		totalCount = 0
		for count in songs[track]['playlists'].itervalues():
			totalCount += len(count)
		if not totalCount > 1:
			continue
		print i, track[0], "by", track[1], "Total count:", totalCount
		duplicates[i] = {'track_name' : track[0], 'artist' : track[1], 'playlists' : {}, 'uri' : songs[track]['uri']}
		for playlist, count in songs[track]['playlists'].iteritems():
			duplicates[i]['playlists'][playlist] = songs[track]['playlists'][playlist]
			print '  ', j, playlist, "count:", len(count), "(Remove all but one)"
			j += 1
			print '  ', j, playlist, "count:", len(count), "(Remove all)"
			j += 1
		print
		j = 1
		i += 1
	input = raw_input( "Which song(s) do you want to remove from which playlist? Type the number of the song followed by the number of the playlist separated by a dot, e.g. 1.1 1.2:")
	
	if input.strip == "exit":
		break
	args = input.strip.split
	i = ""
	j = ""
	
	tracks_list = []
	for playlists, uri in songs.itervalues():
		for playlist in playlists:
			tracks_list.append({'uri' : uri, 'positions' : indexes})
	
	#for str in args:
	#	try:
	#		i = int(str[0])
	#		j = int(str[2])
	#	except:
	#		continue
	#	
	#	if i % 2 == 0:
	#		
	#	else:
			
		
	