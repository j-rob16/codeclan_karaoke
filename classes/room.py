class Room:

    def __init__(self, room_number, capacity, playlist):
        self.room_number = room_number
        self.capacity = capacity
        self.playlist = playlist
        self.occupants = []

    def check_in_guest(self, guest):
        self.occupants.append(guest)

    def check_out_guest(self, guest_name):
        for guest in self.occupants:
            if guest.name == guest_name:
                self.occupants.remove(guest)

