from flask_restful import Resource
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import string


class SearchWords(Resource):
    def get(self, artista, palavra):

        # Página principal com todas as musicas dos artistas
        html = requests.get(f'https://www.vagalume.com.br/{artista.replace(" ", "-").lower()}/')

        # Estruturando dados como html
        soup = BeautifulSoup(html.content, 'html.parser')

        links = []

        # Procura a lista alfabetica e filtra todos as tags a
        for tag in soup.find(id='alfabetMusicList').find_all('a'):
            # Por cada tag pega o conteúdo do atributo href
            caminhno = tag.attrs['href']
            # filtra os links para que não sej adicionado os links com #play no final
            if '#play' not in str(caminhno):
                # Gera o link para acessar a música e adiciona na lista
                links.append('https://www.vagalume.com.br' + caminhno)

        # captura o nome do artista ou banda, removendo o nome da página
        artista_banda = str(soup.title.string).replace(" - VAGALUME", "")
        frases = []

        print('\n' * 2)
        # E por cada link capturado ele busca a palavra por toda a letra, O tqdm é responsavél pela barra de progresso
        for link_musica in links:
            # faz a requisição até a página
            html_musica = requests.get(link_musica)
            # Tratar o conteúdo recebido como um documento como uma estrutura de documento html
            soup = BeautifulSoup(html_musica.content, 'html.parser')

            try:
                # Tenta capturar a letra da música, fazendo uma lista com cada linha(frase)
                for linha in soup.find(id="lyrics").contents:
                    # Faz um for por todos a pontuação fornecida pelo  string.punctuation
                    for item in string.punctuation:
                        # Atualiza a variavel com a frase sem pontuação(remove a pontuação)
                        linha = str(linha).replace(str(item), '')

                    # Cria uma lista com cada palavra da frase
                    for linha_palavra in [linha_palavra.lower() for linha_palavra in linha.split()]:
                        # Se a palavra pesquisada for igual a palavra da frase
                        if palavra.lower() == linha_palavra:
                            # Cria um dicionario como item, colocando o nome da música, frase, e o link ele dentro de
                            # uma lista
                            frases.append(
                                dict(musica=soup.find(id="lyricContent").find('h1').string,
                                     frase=str(linha).lower(), link=link_musica)
                            )
            # Caso algum erro de atributo seja encontrado, apena pula
            except AttributeError as err:
                pass

        # Como as músicas podem ter frases repeticas, criei essa função que
        # Retira as frases repetida de cada música e acrescenta uma linha dentro da tabela
        result = [{'musica': str(i['musica']), 'frase': str(i['frase']), 'link': str(i['link'])}
                  for n, i in enumerate(frases) if i not in frases[n + 1:]]

        return {f"Resultado da palavra '{palavra}' em '{artista_banda}'": result}
