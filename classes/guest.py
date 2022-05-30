class Guest:
    def __init__(self, name, age, favourite_song, wallet):
        self.name = name
        self.age = age
        self.favourite_song = favourite_song
        self.likes_playlist = False
        self.exclamation = ''
        self.wallet = wallet

    def like_the_playlist(self, room):
        for song in room.playlist:
            if song.title == self.favourite_song.title: 
                self.exclamation = 'Whooo!'
        if self.exclamation:
            return self.exclamation
