from tkinter import ttk
from tkinter import *
from pop import *

def panel_album():

    global currentpanel
    currentpanel.pack_forget()

    window_album = PanedWindow(window, width=1080, height=720)
    currentpanel = window_album

    img, album_name, album_artist, album_info, album_score, album_description, album_songs = album_contents()

    global cover
    ctn_cover = Canvas(window_album, width=190, height=190, bd=2, relief="sunken")
    ctn_cover.place(x=20, y=20)
    cover = PhotoImage(file = img)
    ctn_cover.create_image(100, 100, image = cover) 

    name = album_name
    Label_name = Label(window_album, text=name, fg="black", font=('Arial', 80))
    Label_name.place(x=242,y=60)

    artist = album_artist
    Label_artist = Label(window_album, text=artist, fg="black")
    Label_artist.place(x=250,y=170)
    
    info = album_info
    Label_info = Label(window_album, text=info, fg="black")
    Label_info.place(x=250,y=199)

    score = album_score
    Label_score = Label(window_album, text=score, fg="black", font=('Arial', 20))
    Label_score.place(x=170, y=220)

    description = album_description
    Label_description = Label(window_album, text=description, fg="black", wraplength=450, justify="left")
    Label_description.place(x = 20, y = 270)

    songs = album_songs
    Label_songs = Label(window_album, text=songs, fg="black")
    Label_songs.place(x=20,y=350)

    global share_btn
    share_btn= PhotoImage(file="share-icon.png")
    share_label= Label(image=share_btn)
    button_share= Button(window_album, relief = "raised", image=share_btn, borderwidth=0)
    button_share.place(x = 20, y = 220)

    global like_btn
    like_btn= PhotoImage(file="heart-icon.png")
    like_label= Label(image=like_btn)
    button_like= Button(window_album, relief = "raised", image=like_btn, borderwidth=0)
    button_like.place(x = 80, y = 220)

    global stars_btn
    stars_btn= PhotoImage(file="star-icon.png")
    stars_label= Label(image=stars_btn)
    button_stars= Button(window_album, image=stars_btn, borderwidth=0)
    button_stars.place(x = 250, y = 220)

    global stars_btn2
    stars_btn2= PhotoImage(file="star-icon.png")
    stars_label2= Label(image=stars_btn2)
    button_stars2= Button(window_album, image=stars_btn2, borderwidth=0)
    button_stars2.place(x = 285, y = 220)

    global stars_btn3
    stars_btn3= PhotoImage(file="star-icon.png")
    stars_label3= Label(image=stars_btn3)
    button_stars3= Button(window_album, image=stars_btn3, borderwidth=0)
    button_stars3.place(x = 320, y = 220)

    global stars_btn4
    stars_btn4= PhotoImage(file="star-icon.png")
    stars_label4= Label(image=stars_btn4)
    button_stars4= Button(window_album, image=stars_btn4, borderwidth=0)
    button_stars4.place(x = 355, y = 220)

    global stars_btn5
    stars_btn5= PhotoImage(file="star-icon.png")
    stars_label5= Label(image=stars_btn5)
    button_stars5= Button(window_album, image=stars_btn5, borderwidth=0)
    button_stars5.place(x = 390, y = 220)

def panel_adicionar_albuns():

    global currentpanel
    currentpanel.pack_forget()

    window_adicionar_album = PanedWindow(window, width=1080, height=720)
    currentpanel = window_adicionar_album

    lblNome = Label(window_adicionar_album, text = "Nome")
    lblNome.place(x=70, y=70)
    nome = StringVar()
    entryNome = Entry(window_adicionar_album, width=25, textvariable=nome)
    entryNome.place(x=120, y= 70) 

    lblArtista = Label(window_adicionar_album, text = "Artista")
    lblArtista.place(x=70, y=120)
    artista = StringVar()
    entryArtista = Entry(window_adicionar_album, width=25, textvariable=artista)
    entryArtista.place(x=120, y= 120) 

    lblAno = Label(window_adicionar_album, text = "Ano")
    lblAno.place(x=70, y=170)
    ano = IntVar()
    entryAno = Entry(window_adicionar_album, width=25, textvariable=ano)
    entryAno.place(x=120, y= 170) 


    lblGenero = Label(window_adicionar_album, text = "Género")
    lblGenero.place(x=70, y=220)
    generoalbum = StringVar()
    generoalbum.set(0)
    rd1 = Radiobutton(window_adicionar_album, text = "POP", value = "POP", variable= generoalbum)
    rd2 = Radiobutton(window_adicionar_album, text = "HIP-HOP", value = "HIP-HOP", variable= generoalbum)
    rd3 = Radiobutton(window_adicionar_album, text = "K-POP", value = "K-POP", variable= generoalbum)
    rd4 = Radiobutton(window_adicionar_album, text = "ROCK", value = "ROCK", variable= generoalbum)
    rd5 = Radiobutton(window_adicionar_album, text = "R&B", value = "R&B", variable= generoalbum)
    rd6 = Radiobutton(window_adicionar_album, text = "COUNTRY", value = "COUNTRY", variable= generoalbum)
    rd1.place(x= 120, y= 220)
    rd2.place(x= 120, y= 250)
    rd3.place(x= 120, y= 280)
    rd4.place(x= 120, y= 310)
    rd5.place(x=120, y=340)
    rd6.place(x=120, y=370)

    lblQt = Label(window_adicionar_album, text = "Qt músicas")
    lblQt.place(x=70, y=420)
    qt = IntVar()
    entryQt = Entry(window_adicionar_album, width=25, textvariable=qt)
    entryQt.place(x=140, y= 420) 

    lblDuracao = Label(window_adicionar_album, text = "Duração")
    lblDuracao.place(x=370, y=70)
    duracao = StringVar()
    entryDuracao = Entry(window_adicionar_album, width=25, textvariable=duracao)
    entryDuracao.place(x=450, y= 70) 

    lblMetacritic = Label(window_adicionar_album, text = "Metacritic")
    lblMetacritic.place(x=370, y=120)
    metacritic = IntVar()
    entryMetacritic = Entry(window_adicionar_album, width=25, textvariable=metacritic)
    entryMetacritic.place(x=450, y= 120) 

    lblDescricao = Label(window_adicionar_album, text = "Descrição")
    lblDescricao.place(x=370, y=170)
    descricao = StringVar()
    entryDescricao = Entry(window_adicionar_album, width=25, textvariable=descricao)
    entryDescricao.place(x=450, y= 170) 

    lblMusicas = Label(window_adicionar_album, text = "Músicas")
    lblMusicas.place(x=370, y=220)
    musicas=StringVar()
    entryMusicas = Entry(window_adicionar_album, width=25, textvariable=musicas)
    entryMusicas.place(x=450, y= 220) 

    global image1
    image1 = PhotoImage(file = "img\\add.png" )
    btnInserir = Button(window_adicionar_album, image = image1, width=48, height=48, 
                command= lambda: inserir_album(nome.get(), artista.get(), generoalbum.get(), ano.get(), qt.get(), duracao.get(), metacritic.get(), descricao.get(), musicas.get()))
    btnInserir.place(x=400, y= 350)

def panel_filtrar_albuns():
    """
    Painel de consulta com filtros
    """

    global currentpanel
    currentpanel.pack_forget()

    window_consultar_album = PanedWindow(window, width=1080, height=720)
    currentpanel = window_consultar_album


    choice1 = IntVar()
    choice1.set(1) 
    choice2 = IntVar()
    choice2.set(0) 
    choice3 = IntVar()
    choice3.set(0) 
    choice4 = IntVar()
    choice4.set(0) 
    choice5 = IntVar()
    choice5.set(0) 
    choice6 = IntVar()
    choice6.set(0) 

    ck1 = Checkbutton(window_consultar_album, text = "POP", variable = choice1)
    ck2 = Checkbutton(window_consultar_album, text = "K-POP", variable = choice2)
    ck3 = Checkbutton(window_consultar_album, text = "HIP-HOP", variable = choice3)
    ck4 = Checkbutton(window_consultar_album, text = "ROCK", variable = choice4)
    ck5 = Checkbutton(window_consultar_album, text = "R&B", variable = choice5)
    ck6 = Checkbutton(window_consultar_album, text = "COUNTRY", variable = choice6)
    ck1.place(x=50, y=30)
    ck2.place(x=150, y=30)
    ck3.place(x=250, y=30)
    ck4.place(x=350, y=30)
    ck5.place(x=450, y=30)
    ck6.place(x=550, y=30)


    global imagePesq
    imagePesq = PhotoImage(file = "img\\pesquisar.png")

    btnPesquisar = Button(window_consultar_album, width=48, height=48, image = imagePesq, 
            command = lambda: filtrar_albuns(tree, choice1, choice2, choice3, choice4, choice5, choice6, num_albuns))
    btnPesquisar.place(x=650, y= 20)

    tree = ttk.Treeview(window_consultar_album, columns = ("Nome", "Artista", "Género", "Ano"), show = "headings", height = 12, selectmode = "browse")
    tree.column("Nome", width = 220, anchor = "w")
    tree.column("Artista", width = 100, anchor = "c")
    tree.column("Género", width = 220, anchor = "c")
    tree.column("Ano", width = 220, anchor = "c")

    tree.heading("Nome", text = "Nome")
    tree.heading("Artista", text = "Artista")
    tree.heading("Género", text = "Género")
    tree.heading("Ano", text = "Ano")
    tree.place(x=20, y=90)
      
    lbl_num_albuns = Label(window_consultar_album, text = "Nº de álbuns", font = ("Helvetica", "10"))
    lbl_num_albuns.place(x=18, y=360)

    num_albuns = StringVar()
    txt_num_albuns = Entry(window_consultar_album, width=10, textvariable = num_albuns)
    txt_num_albuns.place(x=100, y=360)

class Application:
    def __init__(self, master=None):
        pass

window = Tk()
Application(window)
window.geometry('1080x720')
window.title('Projeto AED')
window.resizable(0,0)

window_main= PanedWindow(window, width=1080, height=720)
window_main.place(x=0,y=0)

currentpanel = window_main


window.mainloop()