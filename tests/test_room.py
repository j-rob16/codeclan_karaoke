import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1, 10, [Song('Billie Jean', 'Michael Jackson')])
        self.guest_1 = Guest('James', 28, 'Billie Jean')

    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_1.capacity)

    def test_room_has_playlist(self):
        self.assertEqual('Billie Jean', self.room_1.playlist[0].title)

    def test_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(self.guest_1, self.room_1.occupants[0])

    def test_can_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_out_guest(self.guest_1.name)
        self.assertEqual(0, len(self.room_1.occupants))
