"""This is to test for Song."""
from song import Song

# Default test for an empty song
song = Song()
songlist = []
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required

# To test the song's initial value
song2 = Song("Amazing Grace", "John Newton", 1779, True)
songlist.append(song2)
song2 = Song("I want to hold your hand)", "The beatles", 1962, False)
songlist.append(song2)
song2 = Song("its now or never)", "Unknown Artist", 1956, True)
songlist.append(song2)
for item in songlist:
    print(item)
