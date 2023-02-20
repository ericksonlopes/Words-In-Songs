class GetSentenceToJsonException(Exception):
    """ Erro ao converter a lista do banco para json """

    def __str__(self):
        return "Erro ao converter a lista do banco para json"
