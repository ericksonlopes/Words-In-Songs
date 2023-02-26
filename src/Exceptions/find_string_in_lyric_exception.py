class FindStringInLyricException(Exception):
    """ Erro ao encontrar a string na letra da música """

    def __init__(self, link: str):
        self.link = link

    def __str__(self):
        return f"Erro ao encontrar a string na letra da música '{self.link}'"
