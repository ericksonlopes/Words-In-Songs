from unittest import TestCase

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestClassWordInSongs(TestCase):
    def setUp(self):
        self.artist = "cazuza"
        self.sentence = "amor"

    def test_wis(self):
        response = client.post("/", json={"artist": self.artist, "sentence": self.sentence})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())

    def test_wis_not_found(self):
        response = client.post("/", json={"artist": "not_found", "sentence": self.sentence})

        self.assertEqual(response.status_code, 404)
