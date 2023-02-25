import json
from typing import List

import redis

from config.redis.get_env_redis import RedisEnvConfig
from src.Exceptions import GetSentenceToJsonException, SetSentenceException
from src.models import SetenceFound


class ConnectRedis:
    def __init__(self) -> None:
        self.__redis_settings = RedisEnvConfig()
        
        redis_pool = redis.ConnectionPool(
            host=self.__redis_settings.HOST,
            port=self.__redis_settings.PORT,
            db=self.__redis_settings.DB,
        )
        redis_client = redis.Redis(connection_pool=redis_pool)

        self.__redis = redis_client

    def __enter__(self):
        return self.__redis

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__redis.close()


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
