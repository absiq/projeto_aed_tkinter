from tkinter import *
from tkinter import messagebox
from pygame import mixer
from tkinter import filedialog 


ficheiro= "databases/albums.txt"
musicas = "databases/musicas.txt"

def cria_id_album():
    last_id = 0
    count_id = 0
    ficheiro = 'databases/albums.txt'
    f = open(ficheiro, 'r', encoding="utf=8")
    dados = f.readlines()
    for i in dados:
        line_split = i.split(';')
        if int(line_split[0]) > last_id:
            last_id = int(line_split[0])
    count_id = last_id + 1
    return count_id

def inserir_album(Nome, Artista, filename, current_var, Ano, Qt, Duracao, Metacritic, Descricao, Musicas):
    filePop=open(ficheiro, "a", encoding="utf-8")
    album_id = cria_id_album()
    linha = str(album_id) + ";" + str(filename) + ";" + str(Nome) + ";" + str(Artista) + ";" + str(current_var) + ";" + str(Ano) + ";" + str(Qt) + " músicas" + ";" + str(Duracao) + ";" + str(Metacritic) + ";" + str(Descricao) + ";" + str(Musicas) + ";0;" + "\n" 
    filePop.write(linha)
    filePop.close()
    messagebox.showeinfo("Álbum", "Álbum inserido com sucesso!")

def album_contents(album_id):

    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        global campos
        campos = linha.split(";")
        if campos[0] == str(album_id):
            print(album_id)
            alb_id = campos[0]
            img = campos[1]
            album_name = campos[2]
            album_artist = campos[3]
            album_info = campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7]
            album_score = campos[8]
            album_description = campos[9]
            return img, album_name, album_artist, album_info, album_score, album_description, alb_id

ficheiroFav= "databases/favoritos.txt"

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

def filtrar_albuns(tree, choice1, choice2, choice3, choice4, choice5, choice6, choice7, num_albuns):
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
        if album.split(";")[4] != "COUNTRY" and album.split(";")[4] != "R&B" and album.split(";")[4] != "ROCK" and album.split(";")[4] != "HIP-HOP" and album.split(";")[4] != "K-POP" and album.split(";")[4] != "POP" and choice7.get():
            tree.insert("", "end", values = (album.split(";")[2],album.split(";")[3], album.split(";")[4], album.split(";")[5] ))
    contar_albuns(tree, num_albuns)

mixer.init()


ficheirosMp3 = "databases\musicasmp3.txt"

fileMP3 = open(ficheirosMp3, "r", encoding="utf-8")
mp3 = fileMP3.readlines()
fileMP3.close()

def play_song(lboxMusicas,album_id):
    index = lboxMusicas.curselection()[0]
    for songs in mp3:
        songs = songs.split(";")
        if songs[0] == str(album_id):
            song = songs[1:][index]
            mixer.music.load(song)
            mixer.music.play()

def pause_song():
    mixer.music.stop()

def contar_albuns(tree, num_albuns):
    num_albuns.set(len(tree.get_children()))


def maisVistos():
    """
    seleciona os 5 albuns mais vistos da aplicacao
    """
    file = open("databases\\albums.txt", 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    viewsList = []
    for line in lines:
        split = line.split(";")
        views = split[-2]
        viewsList.append((views, line))

    top_5_views = sorted(viewsList, key=lambda x: x[0], reverse=True)[:5]

    for view in top_5_views:
        split = view[1].split(";")
        id_album = split[0]
        img_album = split[1]
        nome_album = split[2]
        nome_artista = split[3]
        return(id_album + ";" + img_album  + ";" + nome_album +";" + nome_artista)

    with open("top_5_views.txt", "w", encoding="utf-8") as file:
        for view in top_5_views:
            split = view[1].split(";")
            id_album = split[0]
            img_album = split[1]
            nome_album = split[2]
            nome_artista = split[3]
            file.write(id_album + ";" + img_album  + ";" + nome_album +";" + nome_artista + '\n')

def idsMaisVistos():
    file = open("top_5_views.txt", "r", encoding="utf-8")
    lista = file.readlines()
    ids = []
    for linha in lista:
        split = linha.split(";")
        id_album = split[0]
        ids.append(id_album)
    return ids

ficheiroCategorias = "databases\categorias.txt"
ficheiroMusicas = "databases\\albums.txt"

def ListBoxCategorias(lbCategorias):
    f = open(ficheiroCategorias, "r", encoding="utf-8")
    categorias = f.readlines()
    f.close()
    for categoria in categorias:
        lbCategorias.insert(END, categoria)

def contarAlbum(treeCategorias, numAlbumCat):
    numAlbumCat.set(len(treeCategorias.get_children()))


def filtrarAlbums(treeCategorias, numAlbumCat):
    treeCategorias.delete(*treeCategorias.get_children())

    fileAlbum = open(ficheiroMusicas, "r", encoding="utf-8")
    lista = fileAlbum.readlines()
    fileAlbum.close()
    for musica in lista:
        musica = musica.split(";")
        categoria = musica[4]+ "\n"
        if categoria == texto:
            treeCategorias.insert("", "end", values = (musica[0], musica[2], musica[3], musica[5]))
            
    contarAlbum(treeCategorias, numAlbumCat)

def selecaoItem(lbCategorias):
    id = lbCategorias.curselection()
    global texto
    texto = lbCategorias.get(id)
    return texto

fmaisVistos = "top_5_views.txt"

def lerViews():
    fileViews=open(fmaisVistos, "r", encoding="utf-8")
    lista = fileViews.readlines()
    fileViews.close()
    print(lista)
    return lista


def refreshTreeViews(listaViews, treeVisualicacao):
    treeVisualicacao.delete(*treeVisualicacao.get_children())
    for item in listaViews:
        item = item.split(";")
        treeVisualicacao.insert("", "end", values = (item[0],item[2], item[3], item[4]))

fScore = "databases\\top_5_ratings.txt"

def lerScore():
    fScore = 'databases/top_5_ratings.txt'
    fileScore=open(fScore, "r", encoding="utf-8")
    listaScore = fileScore.readlines()
    fileScore.close()
    lista = []
    for line in listaScore:
        campos = line.split(';')
        img, album_name, album_artist, album_info, album_score, album_description, alb_id = album_contents(campos[0])
        new_line = campos[0] + ';' + img + ';' + album_name + ';' + album_artist + ';' + campos[1]
        lista.append(new_line)
    return lista

lerScore()

def refreshTreeAval(listaAvaliacao, treeAvaliacao):
    treeAvaliacao.delete(*treeAvaliacao.get_children())
    for item in listaAvaliacao:
        item = item.split(";")
        treeAvaliacao.insert("", "end", values = (item[0],item[2], item[3], item[4]))
