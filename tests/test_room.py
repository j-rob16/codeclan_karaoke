import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1, 10, [Song('Billie Jean', 'Michael Jackson')])
        self.small_room = Room(2, 2, ['Bulls On Parade', 'Billie Jean'])

        self.guest_1 = Guest('James', 28, 'Bulls On Parade')
        self.guest_2 = Guest('Kyle', 20, 'Billie Jean')
        self.guest_3 = Guest('Ben', 17, 'Bulls On Parade')

        self.song_1 = Song('Bulls On Parade', 'Rage Against The Machine')
        self.song_2 = Song('Billie Jean', 'Michael Jackson')

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

    def test_can_add_song_to_room(self):
        self.room_1.add_song(self.song_1)
        self.assertIn(self.song_1, self.room_1.playlist)

    def test_room_is_full(self):
        self.small_room.check_in_guest(self.guest_1)
        self.small_room.check_in_guest(self.guest_2)
        self.small_room.check_in_guest(self.guest_3)
        self.assertEqual(self.small_room.capacity, len(self.small_room.occupants))
        self.assertNotIn(self.guest_3, self.small_room.occupants)