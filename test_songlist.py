"""This is to test for List of Song"""

from songlist import SongList
from song import Song
from operator import attrgetter

# Empty SongList test
song_list = SongList()
assert len(song_list.songs) == 0

# Songs load testing
song_list.load_songs('songs.csv')
assert len(song_list.songs) > 0  # assuming CSV file is not empty
print(song_list)
# Test to get the number of song(s) to learn
print("Number of songs to learn = ", song_list.get_number_required())

# Test to sort songs out
song_list.sort_list("Required")
print('\n\n', song_list)
# Test to add new song
song_list.add_song("Here and Now","Someone",1981,False)
print(song_list)

# Separately test to get number of learnt and required songs
print("Number of songs learnt = ", song_list.get_number_learned())
# Test to save songs (will check the CSV file manually to see the end results)
song_list.save_songs("songs.csv")
