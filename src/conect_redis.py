import json
from typing import List

import redis

from config import RedisEnvConfig
from src.Exceptions import GetSentenceToJsonException, SetSentenceException
from src.models import SetenceFound


class ConnectRedis:
    def __init__(self) -> None:
        redis_pool = redis.ConnectionPool(
            host=RedisEnvConfig.HOST,
            port=RedisEnvConfig.PORT,
            db=RedisEnvConfig.DB,
        )
        self.__redis = redis.Redis(connection_pool=redis_pool)

    def __enter__(self):
        return self.__redis

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__redis.close()


class RandlerRedis:
    def get_found_sentense_to_json(self, key: str) -> dict or bool:
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
            str_list_sentence = str(list(map(lambda setence_found: setence_found.__dict__, values)))

            with ConnectRedis() as self.__redis:
                self.__redis.hset(key, "found", str_list_sentence)
                self.__redis.expire(key, 1000)
        except Exception:
            raise SetSentenceException
