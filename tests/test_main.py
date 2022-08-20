from unittest import TestCase
from src.words_in_songs import WordInSongs


class TestWordInSongs(TestCase):

    def setUp(self):
        self.artist = "cazuza"
        self.sentence = "amor"

    def test_get_links_music(self):
        WordInSongs(self.artist, self.sentence)

    def test_find_string_in_lyrics(self):
        wsi = WordInSongs(self.artist, self.sentence)
        lista_links = wsi.get_links_musics()
        wsi.find_string_in_lyrics(lista_links)

    def test_view_table(self):
        wsi = WordInSongs(self.artist, self.sentence)
        lista_links = wsi.get_links_musics()
        lista_lyrics = wsi.find_string_in_lyrics(lista_links)
        wsi.view_table(lista_lyrics)

