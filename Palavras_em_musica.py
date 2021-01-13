import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from tqdm import tqdm
import string

palavra = 'amar'

# Página principal com todas as musicas dos artistas
html = requests.get('https://www.vagalume.com.br/legiao-urbana/')

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

artista_banda = str(soup.title.string).replace(" - VAGALUME", "")
frases = []

print('\n' * 2)
for link_musica in tqdm(links, desc=f'Pesquisando "{palavra.capitalize()}" '
                                    f'por todas as músicas de "{artista_banda}"'):
    html_musica = requests.get(link_musica)
    soup = BeautifulSoup(html_musica.content, 'html.parser')
    try:
        for linha in soup.find(id="lyrics").contents:
            for item in string.punctuation:
                linha = str(linha).replace(str(item), '')

            for linha_palavra in [linha_palavra.lower() for linha_palavra in linha.split()]:
                if palavra.lower() == linha_palavra:
                    frases.append(
                        dict(musica=soup.find(id="lyricContent").find('h1').string,
                             frase=str(linha).lower(), link=link_musica)
                    )
    except AttributeError as err:
        pass

print('\n' * 2)

tabela_final = PrettyTable(['Música', 'Frase com a Palavra encontrada', 'link da letra'])

[tabela_final.add_row(
    [str(i['musica']), str(i['frase']), str(i['link'])]) for n, i in enumerate(frases) if i not in frases[n + 1:]]

print(f"Resultado da '{palavra}' em '{artista_banda}'")
print(tabela_final)
