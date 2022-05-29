import unittest

from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1, 10, [Song('Billie Jean', 'Michael Jackson')])

    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_1.capacity)

    def test_room_has_playlist(self):
        self.assertEqual('Billie Jean', self.room_1.playlist[0].title)