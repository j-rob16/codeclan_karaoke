import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest('James', 28, 'Billie Jean', 70)
        self.room = Room(1, 10, Song('Billie Jean', 'Michael Jackson'))

    def test_guest_has_name(self):
        self.assertEqual('James', self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(28, self.guest.age)

    def test_guest_has_favourite_song(self):
        self.assertEqual('Billie Jean', self.guest.favourite_song)

    def test_guest_has_wallet(self):
        self.assertEqual(70, self.guest.wallet)

    def test_guest_pays_for_room(self):
        self.room.collect_entry_fee(self.guest)
        self.assertEqual(60, self.guest.wallet)