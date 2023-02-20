class SetSentenceException(Exception):
    """ Retorna uma exceção quando não consegue salvar os objetos no redis """

    def __str__(self):
        return "Erro ao salvar os objetos no redis"
