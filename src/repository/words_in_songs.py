from typing import List

import requests
from bs4 import BeautifulSoup
from loguru import logger

from src.Exceptions import ArtistNotFoundException, FindStringInLyricException
from src.models import SetenceFound


class WordInSongs:
    """ Classe responsável por buscar as músicas do artista e as frases que contenham a palavra """
    __URL_VAGALUME = 'https://www.vagalume.com.br/'

    def __init__(self, artist: str, sentence: str):

        self.__artist = artist
        self.__sentence = sentence
        self.__soup_html: BeautifulSoup

        self.__setence_found_list: List[SetenceFound] = []
        self.__links_musics: List[str] = []

        # Página principal com todas as músicas dos artistas
        html = requests.get(f'{self.__URL_VAGALUME}/{self.__artist.replace(" ", "-").lower()}/')

        if html.status_code == 404:
            logger.warning(f"O artista '{self.__artist}' não foi encontrado.")
            raise ArtistNotFoundException(f"O artista '{self.__artist}' não foi encontrado.")

        # Estruturando dados como html
        self.__soup_html = BeautifulSoup(html.content, 'html.parser')

        # Captura o nome do artista
        self.__artist = str(self.__soup_html.title.string).replace(" - VAGALUME", "")

    def sentence_found_list(self) -> List[SetenceFound]:
        return self.__setence_found_list

    @property
    def artist(self):
        return self.__artist

    @property
    def sentence(self):
        return self.__sentence

    def get_links_musics(self) -> List[str]:
        """ Captura todos os links das músicas do artista """

        try:
            # Procura a lista alfabetica e filtra todos as tags a
            for tag in self.__soup_html.find(id='alfabetMusicList').find_all('a'):
                # Por cada tag pega o conteúdo do atributo href
                path = tag.attrs['href']
                # filtra os links para que não sej adicionado os links com #play no final
                if '#play' not in str(path):
                    full_path = self.__URL_VAGALUME + path
                    self.__links_musics.append(full_path)

                    # Gera o link para acessar a música e adiciona na lista
                    yield full_path
        except Exception:
            logger.warning(f"Erro ao capturar os links das músicas do artista '{self.__artist}'")
            raise ArtistNotFoundException(self.__artist)

    def find_string_in_lyric(self, link: str) -> None:
        """ Procura a ‘string’ em todas as letras das músicas do artista """

        try:
            # faz a requisição até a página
            html_musica = requests.get(link)
            # Tratar o conteúdo recebido como um documento como uma estrutura de documento html
            soup = BeautifulSoup(html_musica.content, 'html.parser')

            page_music = []
            try:

                for item in soup.find(id="lyrics").contents:
                    page_music.append(item)

            except AttributeError:
                pass

            phases = [item.text for item in page_music if item.text != '']
            musica = soup.find(id="lyricContent").find('h1').string

            for phase in phases:
                if not self.sentence.lower() in phase.lower():
                    continue

                if phase not in page_music:
                    continue

                if phase in [item.phase for item in self.__setence_found_list]:
                    continue

                if musica is None or phase is None or link is None:
                    continue

                self.__setence_found_list.append(SetenceFound(music=musica, phase=phase, link=link))

        except Exception:
            logger.warning(f"Erro ao encontrar a string na letra da música '{link}'")
            raise FindStringInLyricException(link)
