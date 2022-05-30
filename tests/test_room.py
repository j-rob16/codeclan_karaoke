import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1, 10, [Song('Billie Jean', 'Michael Jackson')])
        self.small_room = Room(2, 2, [Song('Bulls On Parade', 'Rage Against The Machine'), Song('Billie Jean', 'Michael Jackson')])

        self.guest_1 = Guest('James', 28, Song('Bulls On Parade', 'Rage Against The Machine'), 70.0)
        self.guest_2 = Guest('Kyle', 20, Song('Billie Jean', 'Michael Jackson'), 60.0)
        self.guest_3 = Guest('Ben', 17, Song('Bulls On Parade', 'Rage Against The Machine'), 7.0)

        self.song_1 = Song('Bulls On Parade', 'Rage Against The Machine')
        self.song_2 = Song('Billie Jean', 'Michael Jackson')

    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_1.capacity)

    def test_room_has_playlist(self):
        self.assertEqual('Billie Jean', self.room_1.playlist[0].title)

    def test_room_has_till(self):
        self.assertEqual(100.0, self.room_1.till)

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

    def test_can_add_to_till(self):
        self.room_1.collect_entry_fee(self.guest_1)
        self.assertEqual(110.0, self.room_1.till)

    def test_guest_can_enter_with_no_money(self):
        self.small_room.check_in_guest(self.guest_1)
        self.assertNotIn(self.guest_3, self.small_room.occupants)

    def test_customer_likes_the_playlist(self):
        self.room_1.check_in_guest(self.guest_2)
        self.assertEqual('Whooo!', self.guest_2.exclamation)

