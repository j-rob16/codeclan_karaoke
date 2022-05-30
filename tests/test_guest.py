import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest('James', 28, 'Billie Jean', 70)

    def test_guest_has_name(self):
        self.assertEqual('James', self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(28, self.guest.age)

    def test_guest_has_favourite_song(self):
        self.assertEqual('Billie Jean', self.guest.favourite_song)