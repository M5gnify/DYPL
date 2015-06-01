SDR stands for Spotify Duplicate Remover.
The program will list all songs that have duplicates and which playlist they're in, grouped by song. Then you get to remove duplicates by specifying which song should be removed from which playlist.

First install Spotipy: http://spotipy.readthedocs.org/en/latest/#installation. If you have Python version 2.7.9+ or 3.4+ installed, you can run the pip command, otherwise install pip or download the Spotipy source and run setup.py

You have to reqeust an access token to run the program. Here's how to do it:
1. Go to: https://developer.spotify.com/web-api/console/get-current-user-saved-tracks/
2. Click on "GET OAUTH TOKEN"
3. Mark the "user-library-read" scope and click "REQUEST TOKEN"
4. Log in to Spotify and accept 
5. Copy the access token
6. Assign the token to the "token" variable in SDR.py
7. Assign your Spotify username to the "username" variable in SDR.py
8. Run the program without arguments in a console.

Limitations:
1. The program will not count the playlist "Starred" as a playlist.
2. The program will not list songs that are local.
3. The program will not run if your Spotify username contains "едц" and maybe other special characters.