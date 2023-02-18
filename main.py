import asyncio
import concurrent.futures
from typing import List

from fastapi import FastAPI

from src.models import ArtistSentence, SetenceFound
from src.words_in_songs import WordInSongs

app = FastAPI()


@app.post("/")
async def wsi(artist_sentence: ArtistSentence) -> List[SetenceFound]:
    word_songs = WordInSongs(artist_sentence.artist, artist_sentence.sentence)
    get_links_musics = word_songs.get_links_musics()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(executor, word_songs.find_string_in_lyric, link) for link in get_links_musics]

        await asyncio.gather(*tasks)

    return word_songs.sentence_found_list()
