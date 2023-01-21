from tkinter import *

def panel_genre(genre):

    global currentpanel
    currentpanel.pack_forget()

    generos = PanedWindow(generos, width=1080, height=720)
    currentpanel = generos

    generoAPesquisar = genre
    
    f = open("pop.txt", "r", encoding="utf-8")
    arquivo = f.readlines()
    f.close()
    for linha in arquivo:
        for linhas in linha:
            sep = linha.split(";")
        i = 0
        img = linha[i][1] 
        name = linha[i][2]
        artist = linha[i][3]
        for i in linha:
            print (img, name, artist)
            

    generos.mainloop()

panel_genre("POP")