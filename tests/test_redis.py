from config import ConnectRedis, RandlerRedis
from src.models import SetenceFound


class TestRedis:
    def test_get_found_sentence_to_json(self):
        with ConnectRedis() as redis:
            redis.set("test", "test")
            assert redis.get("test") == b"test"
            redis.delete("test")
            assert redis.get("test") is None

    def test_set_sentence_found(self):
        randler = RandlerRedis()
        key = "test:test"
        randler.set_sentence_found(key, [SetenceFound(music="musica", phase="phase", link="link"), ])
        assert randler.get_found_sentence_to_json(key) == [{"music": "musica", "phase": "phase", "link": "link"}]
