class ArtistNotFoundException(Exception):
    """ Artista não encontrado """

    def __init__(self, artist: str):
        self.artist = artist

    def __str__(self):
        return f"Artista '{self.artist}' não encontrado"
