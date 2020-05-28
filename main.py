"""
Author: Arifin Sugawa
Date: 22/04/2020
Brief Project Description:
A program for user to save their favorite songs that they had learnt
as well as keeping track and recording upcoming songs that they want to learn.
GitHub URL: https://github.com/arifinsugawa/CP1404Assignments_ArifinSugawa_jc261529
"""

from kivy.app import App
from kivy.lang import Builder
from songlist import SongList
from kivy.uix.button import Button
# This is for the main program which uses the SongsToLearnApp class

FILE_NAME = 'songs.csv'

class SongsToLearnApp(App):
    def build(self):
        self.title = "Songs to learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.root.ids.sort_options.values = self.song_list_options
        self.song_button_creator()
        return self.root

    def __init__(self):
        super().__init__()
        self.song_list = SongList()
        self.song_list.load_songs(FILE_NAME)
        self.song_list.sort_list("Artist")
        self.song_list_options = ['Artist', 'Title', 'Year', 'Required']

    def song_button_creator(self):
        for item in self.song_list.songs:
            new_button = Button(text = str(item))
            self.root.ids.song_buttons.add_widget(new_button)

    def song_sorter(self):
        self.song_list.sort_list(self.root.ids.sort_options.text)
        self.root.ids.song_buttons.clear_widgets()
        self.song_button_creator()

    def handle_add_song(self):
        if self.root.ids.song_title.text == '' or \
           self.root.ids.song_artist.text == '' or \
           self.root.ids.song_year.text == '':
           self.root.ids.label_text_id.text = 'All fields must be completed'
        elif int(self.root.ids.song_year.text) < 0:
            self.root.ids.label_text_id.text = 'Year must be >= 0'
        elif not (self.root.ids.song_year.text.isdigit()):
            self.root.ids.label_text_id.text = 'Please enter a valid number'
        else:
            self.song_list.add_song(self.root.ids.song_title.text, self.root.ids.song_artist.text, \
                               self.root.ids.song_year.text, False)
            self.root.ids.label_text_id.text = self.root.ids.song_title.text + ' added'
            self.song_list.sort_list(self.root.ids.sort_options.text)
            self.root.ids.song_buttons.clear_widgets()
            self.song_button_creator()

    def clear_fields(self):
        self.root.ids.song_title.text = ''
        self.root.ids.song_artist.text = ''
        self.root.ids.song_year.text = ''
        self.root.ids.label_text_id.text = ''

    def change_learned(self):
        pass

    def __del__(self):
        self.song_list.save_songs(FILE_NAME)
        print(self.song_list)

SongsToLearnApp().run()
