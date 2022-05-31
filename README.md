# Words-In-Songs

![Star](https://img.shields.io/github/stars/Erickson-lopes-dev/Words-In-Songs?style=social) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Erickson_Lopes%20-blue)](https://www.linkedin.com/in/ericksonlopes/)

Este projeto gira em torno de uma ideia "E se eu criar uma ferramente onde eu possa pesquisar por todas as músicas de um artista uma determinada frase ou palavra"


- Basta chamar a classe e passar os parâmetros correspondentes
```python
wsi = WordInSongs(artist="cazuza", sentence="meu amor")
wsi.show()
```

- Saída no terminal do código acima:
```commandline
Pesquisando "Meu amor" por todas as músicas de "Cazuza": 100%|██████████| 125/125 [00:11<00:00, 10.78it/s]
+-----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------+
|         Música        |                     Frase com a Palavra encontrada                    |                         link da letra                         |
+-----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------+
|  A Orelha de Eurídice |                          É a prova, meu amor                          |  https://www.vagalume.com.br/cazuza/a-orelha-de-euridice.html |
|  A Orelha de Eurídice |                          Resgatar o meu amor                          |  https://www.vagalume.com.br/cazuza/a-orelha-de-euridice.html |
|      Bete Balanço     |                         Bete balança meu amor                         |      https://www.vagalume.com.br/cazuza/bete-balanco.html     |
|    Bilhetinho Azul    |               o meu amor foi embora e só deixou pra mim               |    https://www.vagalume.com.br/cazuza/bilhetinho-azul.html    |
|  Codinome Beija-Flor  |                  Não responda nunca, meu amor (nunca)                 |  https://www.vagalume.com.br/cazuza/codinome-beija-flor.html  |
|        Cúmplice       |                         Meu amor, meu cúmplice                        |        https://www.vagalume.com.br/cazuza/cumplice.html       |
| E Estamos Conversados | falem longe da minha janela por favor, se for para falar do meu amor. | https://www.vagalume.com.br/cazuza/e-estamos-conversados.html |
| Faz Parte do Meu Show |                          Com todo o meu amor                          | https://www.vagalume.com.br/cazuza/faz-parte-do-meu-show.html |
| Faz Parte do Meu Show |                    Faz parte do meu show, meu amor                    | https://www.vagalume.com.br/cazuza/faz-parte-do-meu-show.html |
|       Maioridade      |                       Mas meu amor não é ficção                       |       https://www.vagalume.com.br/cazuza/maioridade.html      |
|   Orelha de Eurídice  |             é a prova, meu amor, me espera sem uma orelha             |   https://www.vagalume.com.br/cazuza/orelha-de-euridice.html  |
|   Orelha de Eurídice  |             vou correndo, vou agora, resgatar o meu amor.             |   https://www.vagalume.com.br/cazuza/orelha-de-euridice.html  |
|        Portuga        |                        Pelo meu amor pelo acaso                       |        https://www.vagalume.com.br/cazuza/portuga.html        |
|      Preconceito      |                     Por que meu amor este abraço?                     |      https://www.vagalume.com.br/cazuza/preconceito.html      |
|    Só se For a Dois   |                         São egoístas, meu amor                        |    https://www.vagalume.com.br/cazuza/so-se-for-a-dois.html   |
+-----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------+
```