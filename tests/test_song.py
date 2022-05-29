import unittest 

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song('Billie Jean', 'Michael Jackson')

    def test_song_has_name(self):
        self.assertEqual('Billie Jean', self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual('Michael Jackson', self.song_1.artist)