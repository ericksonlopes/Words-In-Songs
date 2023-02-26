import json
from typing import List

from config import ConnectRedis
from src.Exceptions import GetSentenceToJsonException, SetSentenceException
from src.models import SetenceFound


class RandlerRedis:
    @staticmethod
    def get_found_sentence_to_json(key: str) -> dict or bool:
        try:
            with ConnectRedis() as r:
                if r.exists(key):
                    response = r.hget(key, "found")
                    response = response.decode("utf-8").replace("'", '"')

                    dicio = json.loads(response)
                    return dicio

        except Exception:
            raise GetSentenceToJsonException

        return False

    def set_sentence_found(self, key, values: List[SetenceFound]):
        try:
            str_list_sentence = str(list(map(lambda sentence_found: sentence_found.__dict__, values)))

            with ConnectRedis() as self.__redis:
                self.__redis.hset(key, "found", str_list_sentence)
                self.__redis.expire(key, 1000)
        except Exception:
            raise SetSentenceException
