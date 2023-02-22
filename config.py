import os

from pydantic.dataclasses import dataclass


@dataclass
class RedisEnvConfig:
    PORT = os.getenv('REDIS_PORT') or 6379
    HOST = os.getenv('REDIS_HOST') or 'localhost'
    DB = os.getenv('REDIS_DB')  or 0
