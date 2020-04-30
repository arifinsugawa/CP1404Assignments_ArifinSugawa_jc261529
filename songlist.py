# This is for songlist
from song import Song
from operator import attrgetter

class SongList:
    def __init__(self):
        self.songs = []

    def get_title(self, title):
        for item in song_list:
            if item[0] == title:
                return item

        return title + " not in list"

    def add_song(self, title, artist, year, is_required):
        self.songs.append(Song(title, artist, year, is_required))

    def get_number_required(self):
        count = 0
        for item in self.songs:
            if item.is_required == 'n':
                count += 1
        return count

    def get_number_learned(self):
        number_learnt = 0
        for item in self.songs:
            if item.is_required == 'y':
                number_learnt += 1
        return number_learnt

    def load_songs(self, file_name):
        try:
            in_file = open(file_name, 'r')
            for line in in_file:
                a_song = line.strip('\n').split(',')
                self.add_song(a_song[0], a_song[1], a_song[2], a_song[3])
            in_file.close()
        except:
            print("Error - File empty no songs to load")

    def save_songs(self, file_name):
        out_file = open(file_name, 'w')
        for item in self.songs:
            print(item.title + ',' + item.artist + ',' + str(item.year) + ',' + \
                  (('n', 'y')[item.is_required == True]), file=out_file)
        out_file.close()

    def sort_list(self, sorting_key):
        if sorting_key == 'Required':
            sorting_key = 'is_required'
        if sorting_key != "title":
            self.songs.sort(key=attrgetter(sorting_key.lower(), "title"))
        else:
            self.songs.sort(key=attrgetter(sorting_key.lower()))

    def __str__(self):
        a_string = ''
        for i in range(len(self.songs)):
            a_string = a_string + self.songs[i].__str__() + '\n'
        return a_string