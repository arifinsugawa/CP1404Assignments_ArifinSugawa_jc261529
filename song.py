
class Song:
    def __init__(self, title='', artist='', year=0, is_required='y'):
        self.artist = artist.title()
        self.title = title.title()
        self.year = int(year)
        if is_required.lower() == 'y':
            self.is_required = False
        elif is_required.lower() == 'n':
            self.is_required = True
        else:
            self.is_required = is_required

    def set_learnt(self):
        self.is_required = True

    def set_not_learnt(self):
        self.is_required = False

    def __str__(self):
        return "\'{}\' by {} ({:4}) {}".format(self.title, self.artist, self.year, (('(learned)', '')[self.is_required==False]))
