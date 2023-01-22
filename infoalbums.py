from tkinter import *
from tkinter import messagebox
from pygame import mixer


ficheiro= "databases/albums.txt"
musicas = "databases/musicas.txt"

def cria_id_album():
    last_id = 0
    count_id = 0
    ficheiro = 'databases/albums.txt'
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
    linha = str(album_id) + ";" + "imgs/No-Image.png" + ";" + str(Nome) + ";" + str(Artista) + ";" + str(generoalbum) + ";" + str(Ano) + ";" + str(Qt) + " músicas" + ";" + str(Duracao) + ";" + str(Metacritic) + ";" + str(Descricao) + ";" + str(Musicas) + "\n" 
    filePop.write(linha)
    filePop.close()

#def album_contents(album_id):
def album_contents():

    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        global campos
        campos = linha.split(";")
        #if campos[0] == str(album_id):
        if campos[0] == "2":
            #print(album_id)
            img = campos[1]
            album_name = campos[2]
            album_artist = campos[3]
            album_info = campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7]
            album_score = campos[8]
            album_description = campos[9]
            
            return img, album_name, album_artist, album_info, album_score, album_description

ficheiroFav= "databases/favoritos.txt"

def likeList():
    favoritos = open(ficheiroFav, "a", encoding="utf-8")
    infoAlb = campos[0] + ";" + campos[1] + ";" + campos[2] + ";" + campos[3] + ";" + campos[4] + ";" + campos[5] + ";" + campos[6] + ";" + campos[7] + ";" + campos[8] + ";" + campos[9] 
    favoritos.write(infoAlb)
    favoritos.close()

ficheiroReviews = "databases/reviews.txt"

def reviewsList(numberStars):
    reviews = open(ficheiroReviews, "a", encoding="utf-8")
    if numberStars == 1:
        writeFile = campos[0] + ";" + "one star" + "\n"
        reviews.write(writeFile)
    elif numberStars == 2:
        writeFile = campos[0] + ";" + "two stars" + "\n"
        reviews.write(writeFile)
    elif numberStars == 3:
        writeFile = campos[0] + ";" + "three stars" + "\n"
        reviews.write(writeFile)
    elif numberStars == 4:
        writeFile = campos[0] + ";" + "four stars" + "\n"
        reviews.write(writeFile)
    elif numberStars == 5:
        writeFile = campos[0] + ";" + "five stars" + "\n"
        reviews.write(writeFile)
    reviews.close()
            

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

mixer.init()


ficheirosMp3 = "databases\musicasmp3.txt"

fileMP3 = open(ficheirosMp3, "r", encoding="utf-8")
mp3 = fileMP3.readlines()
fileMP3.close()

def play_song(lboxMusicas):
    index = lboxMusicas.curselection()[0]
    for songs in mp3:
        songs = songs.split(";")
        if songs[0] == "2":
            song = songs[1:][index]
            mixer.music.load(song)
            mixer.music.play()

def pause_song():
    mixer.music.stop()