class ArtistNotFound(Exception):
    """ Artista não encontrado """

    def __str__(self):
        return "Artista não encontrado"
