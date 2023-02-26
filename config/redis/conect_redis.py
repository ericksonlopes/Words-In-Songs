import redis

from config.redis.get_env_redis import RedisEnvConfig


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
