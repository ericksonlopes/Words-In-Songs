import requests
from typing import List
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from utils import *


class WordInSongs:
    def __init__(self, artist, sentence):
        self.__artist = artist
        self.__sentence = sentence
        self.__soup_html: BeautifulSoup

        # Página principal com todas as musicas dos artistas
        html = requests.get(f'https://www.vagalume.com.br/{self.__artist.replace(" ", "-").lower()}/')

        if html.status_code == 404:
            raise ArtistNotFound(f"O artista '{self.__artist}' não foi encontrado.")

        # Estruturando dados como html
        self.__soup_html = BeautifulSoup(html.content, 'html.parser')

        # Captura o nome do artista
        self.__artist = str(self.__soup_html.title.string).replace(" - VAGALUME", "")

    @property
    def artist(self):
        return self.__artist

    @property
    def sentence(self):
        return self.__sentence

    def get_links_music(self) -> List[str]:

        links = []

        # Procura a lista alfabetica e filtra todos as tags a
        for tag in self.__soup_html.find(id='alfabetMusicList').find_all('a'):
            # Por cada tag pega o conteúdo do atributo href
            path = tag.attrs['href']
            # filtra os links para que não sej adicionado os links com #play no final
            if '#play' not in str(path):
                # Gera o link para acessar a música e adiciona na lista
                links.append('https://www.vagalume.com.br' + path)

        return links

    def find_string_in_lyrics(self, links: list) -> List[SetenceFound]:
        phases = []
        # E por cada link capturado ele busca a palavra por toda a letra, O tqdm é responsavél pela barra de progresso
        for link_music in links:
            # faz a requisição até a página
            html_musica = requests.get(link_music)
            # Tratar o conteúdo recebido como um documento como uma estrutura de documento html
            soup = BeautifulSoup(html_musica.content, 'html.parser')

            page_music = []
            try:

                for item in soup.find(id="lyrics").contents:
                    page_music.append(item)

            except AttributeError:
                pass

            paragrafos = [item.text for item in page_music if item.text != '']
            musica = soup.find(id="lyricContent").find('h1').string
            for paragrafo in paragrafos:
                if self.sentence.lower() in paragrafo.lower():
                    phases.append(SetenceFound(music=musica, phase=paragrafo, link=link_music))

        return phases

    @classmethod
    def view_table(cls, phases: List[SetenceFound]) -> PrettyTable:

        # Cria o objeto da tabela, ja com o nome de cada coluna
        tabela_final = PrettyTable(['Música', 'Frase com a Palavra encontrada', 'link da letra'])

        [tabela_final.add_row([str(i.music), str(i.phase), str(i.link)]) for i in phases]

        return tabela_final
