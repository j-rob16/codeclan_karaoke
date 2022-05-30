class Room:

    def __init__(self, room_number, capacity, playlist):
        self.room_number = room_number
        self.capacity = capacity
        self.playlist = playlist
        self.occupants = []
        self.till = 100.0
        self.entry_fee = 10.0

    def check_in_guest(self, guest):
        if self.capacity > len(self.occupants):
            self.occupants.append(guest)
        guest.like_the_playlist(self)

    def check_out_guest(self, guest_name):
        for guest in self.occupants:
            if guest.name == guest_name:
                self.occupants.remove(guest)

    def add_song(self, song):
        self.playlist.append(song)

    def collect_entry_fee(self, guest):
        if guest.wallet >= self.entry_fee:
            guest.wallet -= self.entry_fee
            self.till += self.entry_fee


