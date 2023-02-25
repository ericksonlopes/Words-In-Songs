import asyncio
import concurrent.futures
from typing import List

from fastapi import HTTPException
from loguru import logger

from config import RandlerRedis
from src.Exceptions import ArtistNotFoundException
from src.models import SetenceFound
from src.repository.words_in_songs import WordInSongs


class WordInSongsController:
    @classmethod
    async def get(cls, artist: str, sentence: str) -> List[SetenceFound]:

        key = f"{artist}:{sentence}"
        randler_redis = RandlerRedis()

        logger.info(f"Buscando no redis a chave {key}")

        response = randler_redis.get_found_sentence_to_json(key)
        if response:
            logger.info(f"Dados encontrado no redis a chave {key}")
            return response

        try:
            word_songs = WordInSongs(artist, sentence)
            get_links_musics = word_songs.get_links_musics()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                loop = asyncio.get_event_loop()

                tasks = [loop.run_in_executor(executor, word_songs.find_string_in_lyric, link) for link in
                         get_links_musics]

                await asyncio.gather(*tasks)

            logger.info(f"Encontrado {len(word_songs.sentence_found_list())} vezes")

        except ArtistNotFoundException as not_found_artist:
            logger.warning(not_found_artist.__str__())
            raise HTTPException(status_code=404, detail=not_found_artist.__str__())

        except Exception as e:
            logger.error(e.__str__())
            raise HTTPException(status_code=500, detail=e.__str__())

        randler_redis.set_sentence_found(
            f"{artist}:{sentence}",
            word_songs.sentence_found_list()
        )

        logger.info(f"Salvo no redis a chave {key}")
        return word_songs.sentence_found_list()
