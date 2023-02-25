from typing import List

from fastapi import APIRouter

from src.controllers.words_in_songs_controller import WordInSongsController
from src.models import ArtistSentence, SetenceFound

wis = WordInSongsController()

wis_router = APIRouter()


@wis_router.post("/wis",
                 response_model=List[SetenceFound],
                 status_code=200,
                 summary="Busca a frase em todas as músicas do artista",
                 description="Busca a frase em todas as músicas do artista")
async def wsi(artist_sentence: ArtistSentence) -> List[SetenceFound]:
    artist = artist_sentence.artist
    sentence = artist_sentence.sentence

    return await wis.get(artist, sentence)
