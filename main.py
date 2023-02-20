import asyncio
import concurrent.futures
from typing import List

from fastapi import FastAPI

from src.conect_redis import RandlerRedis
from src.models import ArtistSentence, SetenceFound
from src.words_in_songs import WordInSongs

app = FastAPI()


@app.post("/")
async def wsi(artist_sentence: ArtistSentence) -> List[SetenceFound]:
    artist = artist_sentence.artist
    sentence = artist_sentence.sentence

    key = f"{artist}:{sentence}"
    randler_redis = RandlerRedis()
    response = randler_redis.get_found_sentense_to_json(key)

    if response:
        return response

    word_songs = WordInSongs(artist, sentence)
    get_links_musics = word_songs.get_links_musics()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(executor, word_songs.find_string_in_lyric, link) for link in get_links_musics]

        await asyncio.gather(*tasks)

    randler_redis.set_sentence_found(
        f"{artist}:{sentence}",
        word_songs.sentence_found_list()
    )

    return word_songs.sentence_found_list()
