from tkinter import *
from tkinter import messagebox

ficheiro= "pop.txt"

def cria_id_album():
    last_id = 0
    count_id = 0
    ficheiro = 'pop.txt'
    f = open(ficheiro, 'r')
    dados = f.readlines()
    for i in dados:
        line_split = i.split(';')
        if int(line_split[0]) > last_id:
            last_id = int(line_split[0])
    count_id = last_id + 1
    return count_id

def inserir_album(Nome, Artista, generoalbum, Ano, Qt, Duracao, Metacritic, Descricao, Musicas):
    filePop=open(ficheiro, "a", encoding="utf-8")
    album_id = cria_id_album()
    linha = str(album_id) + ";" + "imgs/No-Image.png" + ";" + str(Nome) + ";" + str(Artista) + ";" + str(generoalbum) + ";" + str(Ano) + ";" + str(Qt) + " músicas" + ";" + str(Duracao) + ";" + str(Metacritic) + ";" + str(Descricao) + ";" + str(Musicas) + ";0;" "\n" 
    filePop.write(linha)
    filePop.close()
    
# colocar ID do álbum
# músicas

def album_contents(album_id):

    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        campos = linha.split(";")
        # campo = str(campos)
        # songs = campo.split(",")
        # print(songs)
        if campos[0] == str(album_id):
            print(album_id)
            img = campos[1]
            album_name = campos[2]
            album_artist = campos[3]
            album_info = campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7]
            album_score = campos[8]
            album_description = campos[9]
            # for songs in linha:
              #  album_songs = songs[0:]
            return img, album_name, album_artist, album_info, album_score, album_description
            
def contar_albuns(tree, num_albuns):
    num_albuns.set(len(tree.get_children()))

def filtrar_albuns(tree, choice1, choice2, choice3, choice4, choice5, choice6, num_albuns):
    tree.delete(*tree.get_children())

    file=open(ficheiro, "r", encoding="utf-8")
    lista = file.readlines()
    file.close()
    cont=0
    for album in lista:
        if album == "": continue
        if album.split(";")[4] == "POP" and choice1.get():
            tree.insert("", "end", values = (album.split(";")[2],album.split(";")[3], album.split(";")[4], album.split(";")[5] ))
        if album.split(";")[4] == "K-POP" and choice2.get():
            tree.insert("", "end", values = (album.split(";")[2],album.split(";")[3], album.split(";")[4], album.split(";")[5] ))
        if album.split(";")[4] == "HIP-HOP" and choice3.get():
            tree.insert("", "end", values = (album.split(";")[2],album.split(";")[3], album.split(";")[4], album.split(";")[5] ))
        if album.split(";")[4] == "ROCK" and choice4.get():
            tree.insert("", "end", values = (album.split(";")[2],album.split(";")[3], album.split(";")[4], album.split(";")[5] ))
        if album.split(";")[4] == "R&B" and choice5.get():
            tree.insert("", "end", values = (album.split(";")[2],album.split(";")[3], album.split(";")[4], album.split(";")[5] ))
        if album.split(";")[4] == "COUNTRY" and choice6.get():
            tree.insert("", "end", values = (album.split(";")[2],album.split(";")[3], album.split(";")[4], album.split(";")[5] ))
    contar_albuns(tree, num_albuns)


def maisVistos():
    """
    seleciona os 5 albuns mais vistos da aplicacao
    """
    file = open("pop.txt", 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    viewsList = []
    for line in lines:
        split = line.split(";")
        views = int(split[10])
        viewsList.append((views, line))

    top_5_views = sorted(viewsList, key=lambda x: x[0], reverse=True)[:5]

    for view in top_5_views:
        split = view[1].split(";")
        id_album = split[0]
        img_album = split[1]
        nome_album = split[2]
        nome_artista = split[3]
        return(id_album + ";" + img_album  + ";" + nome_album +";" + nome_artista)


def maioresScores():
    """
    seleciona os 5 albuns com o maior Score do metacritic
    """
    file = open("pop.txt", 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    scoresList = []
    for line in lines:
        split = line.split(";")
        score = int(split[8])
        scoresList.append((score, line))

    top_5_scores = sorted(scoresList, key=lambda x: x[0], reverse=True)[:5]

    for score in top_5_scores:
        split = score[1].split(";")
        id_album = split[0]
        nome_album = split[2]
        nome_artista = split[3]
        return(id_album + ";" + nome_album + ";" + nome_artista)


