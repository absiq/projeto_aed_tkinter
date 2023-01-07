from tkinter import *
from tkinter import messagebox

ficheiro= "pop.txt"

def inserir_album(Nome, Artista, generoalbum, Ano, Qt, Duracao, Metacritic, Descricao, Musicas):
    filePop=open(ficheiro, "a", encoding="utf-8")
    linha = "img/No-Image.png" + ";" + str(Nome) + ";" + str(Artista) + ";" + str(generoalbum) + ";" + str(Ano) + ";" + str(Qt) + " músicas" + ";" + str(Duracao) + ";" + str(Metacritic) + ";" + str(Descricao) + ";" + str(Musicas) + "\n" 
    filePop.write(linha)
    filePop.close()
    
# colocar ID do álbum
# músicas

def album_contents():

    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        campos = linha.split(";")
        if campos[0] == "1":
            img = campos[1]
            album_name = campos[2]
            album_artist = campos[3]
            album_info = campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7]
            album_score = campos[8]
            album_description = campos[9]
            album_songs = campos[10]
        return img, album_name, album_artist, album_info, album_score, album_description, album_songs

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
