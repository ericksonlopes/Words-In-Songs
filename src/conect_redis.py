import json
from typing import List

import redis

from src.Exceptions import GetSentenceToJsonException, SetSentenceException
from src.models import SetenceFound


class ConnectRedis:
    __HOST = '0.0.0.0'
    __PORT = 6379
    __DB = 0

    def __init__(self) -> None:
        self.__redis = redis.Redis(host=self.__HOST, port=self.__PORT, db=self.__DB)

    def __enter__(self):
        return self.__redis

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__redis.close()


class RandlerRedis:
    def get_found_sentense_to_json(self, key: str) -> dict or bool:
        try:
            with ConnectRedis() as self.__redis:
                if self.__redis.exists(key):
                    response = self.__redis.hget(key, "found")
                    response = response.decode("utf-8").replace("'", '"')

                    dicio = json.loads(response)
                    return dicio

        except Exception:
            raise GetSentenceToJsonException

        return False

    def set_sentence_found(self, key, values: List[SetenceFound]):
        try:
            str_list_sentence = str(list(map(lambda setence_found: setence_found.__dict__, values)))

            with ConnectRedis() as self.__redis:
                self.__redis.hset(key, "found", str_list_sentence)
                self.__redis.expire(key, 1000)
        except Exception:
            raise SetSentenceException
