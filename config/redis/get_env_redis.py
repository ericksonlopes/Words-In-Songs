import os

from pydantic import BaseSettings


class RedisEnvConfig(BaseSettings):
    PORT = os.getenv('REDIS_PORT') or 6379
    HOST = os.getenv('REDIS_HOST') or 'localhost'
    DB = os.getenv('REDIS_DB') or 0
