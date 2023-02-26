class GetLinksMusicsException(Exception):
    """ Erro ao capturar os links das músicas do artista """

    def __init__(self, artist: str):
        self.artist = artist

    def __str__(self):
        return f"Erro ao capturar os links das músicas do artista '{self.artist}'"
