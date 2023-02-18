from pydantic import BaseModel


class ArtistSentence(BaseModel):
    artist: str
    sentence: str
