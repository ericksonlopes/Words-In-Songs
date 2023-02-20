import asyncio
import concurrent.futures
from unittest import TestCase

from src.Exceptions import ArtistNotFoundException
from src.words_in_songs import WordInSongs


class TestClassWordInSongs(TestCase):

    def setUp(self):
        self.artist = "cazuza"
        self.sentence = "amor"
        self.wordis = WordInSongs(self.artist, self.sentence)

    def test_find_string_in_lyrics(self):
        get_links_musics = self.wordis.get_links_musics()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            tasks = [loop.run_in_executor(executor, self.wordis.find_string_in_lyric, link) for link in
                     get_links_musics]

            asyncio.gather(*tasks)

        self.assertTrue(self.wordis.sentence_found_list())

    def test_get_links_music(self):
        self.assertTrue(self.wordis.get_links_musics())

    def test_artist_not_found(self):
        with self.assertRaises(ArtistNotFoundException):
            WordInSongs("asdasdas", "amor")

    def test_sentence_not_found(self):
        if len(self.wordis.sentence_found_list()):
            self.fail("Sentence not found")

    def test_get_artist(self):
        self.assertEqual(self.wordis.artist.lower(), self.artist.lower())

    def test_get_sentence(self):
        self.assertEqual(self.wordis.sentence.lower(), self.sentence.lower())
