from tkinter import *
from tkinter import ttk
import os
from users import *
from pop import *

## GUI implementation

#### PAGE SWITCHERS 

def logout_and_change_page(page):
    logout_user()
    page()

def login_and_change_page(username, password, page):
    if submit_login(username, password) == True:
        page()

def generate_page_album(album_id):
    img, album_name, album_artist, album_info, album_score, album_description = album_contents(album_id)
    panel_album(img, album_name, album_artist, album_info, album_score, album_description)

#### MISC FUNCTIONS

def like():
    like_btn['file'] = "imgs\heart-icon-full.png"

def one_star():
   stars_btn['file'] = "imgs\star-icon-full.png"

def two_stars():
    stars_btn['file'] = "imgs\star-icon-full.png"
    stars_btn2['file'] = "imgs\star-icon-full.png"

def three_stars():
    stars_btn['file'] = "imgs\star-icon-full.png"
    stars_btn2['file'] = "imgs\star-icon-full.png"
    stars_btn3['file'] = "imgs\star-icon-full.png"

def four_stars():
    stars_btn['file'] = "imgs\star-icon-full.png"
    stars_btn2['file'] = "imgs\star-icon-full.png"
    stars_btn3['file'] = "imgs\star-icon-full.png"
    stars_btn4['file'] = "imgs\star-icon-full.png"

def five_stars():
    stars_btn['file'] = "imgs\star-icon-full.png"
    stars_btn2['file'] = "imgs\star-icon-full.png"
    stars_btn3['file'] = "imgs\star-icon-full.png"
    stars_btn4['file'] = "imgs\star-icon-full.png"
    stars_btn5['file'] = "imgs\star-icon-full.png"

## - - - - - - - - - - CONTAINER REGISTER - - - - - - - - - - ##

def panel_edit_profile():
    global currentpanel
    currentpanel.pack_forget()

    window_edit_profile = PanedWindow(window, width=1080, height=720)
    currentpanel = window_edit_profile

    window_edit_profile.configure(bg = "#d3d3d3")

    name, username, icon, bio, user_id = retrieve_current_user_data()

    name_text = "Teu nome atual é: " + name
    label_name = Label(window_edit_profile, text=name_text, bg = "#d3d3d3")
    label_name.place(x=20, y=50)

    username_text = "Teu username atual é: " + username
    label_username = Label(window_edit_profile, text=username_text, bg = "#d3d3d3")
    label_username.place(x=400, y=50)

    bio_text = "Tua bio atual é: "
    label_bio_text = Label(window_edit_profile, text=bio_text, bg = "#d3d3d3")
    label_bio = Label(window_edit_profile, justify='center', wraplength=240, text=bio, bg = "#d3d3d3")
    label_bio_text.place(x=20, y=220)
    label_bio.place(x=20, y=240)

    icon_text = "O teu icon atual é: "
    label_icon_text = Label(window_edit_profile, text=icon_text,bg = "#d3d3d3")
    label_icon_text.place(x=740, y=220)
    ficheiro_img = os.path.join('imgs\\profile_pics', icon)
    user_img = Canvas(window_edit_profile, width=100, height=100, bd=0)
    user_img.place(x=740, y=240)
    global img
    img = PhotoImage(file = ficheiro_img)
    user_img.create_image(50,50, anchor=CENTER, image = img)

    label_new_name = Label(window_edit_profile, text="Insira o teu novo nome:", bg = "#d3d3d3")
    label_new_name.place(x=20, y=80)
    new_name = name
    entry_new_name = Entry(window_edit_profile, width=30, textvariable=new_name)
    entry_new_name.place(x=20, y=100)

    label_new_username = Label(window_edit_profile, text="Insira o teu novo username:", bg = "#d3d3d3")
    label_new_username.place(x=400, y=80)
    new_username = username
    entry_new_username = Entry(window_edit_profile, width=30, textvariable=new_username)
    entry_new_username.place(x=400, y=100)

    label_new_bio = Label(window_edit_profile, text="Insira a tua nova bio:", bg = "#d3d3d3")
    label_new_bio.place(x=20, y=290)
    entry_new_bio = Text(window_edit_profile) # usar GET para inserir conteúdo do Text em new_bio
    entry_new_bio.place(x=20, y=310, width=300, height=100)

    btn_editar = Button(window_edit_profile, text='Editar dados', command=lambda: edit_user_data(entry_new_name.get(), entry_new_username.get(), entry_new_bio.get("1.0",'end-1c')))
    btn_editar.place(x=540, y=600)

    window_edit_profile.place(x=0, y=0)

def panel_register():
    global currentpanel
    currentpanel.pack_forget()

    window_register = PanedWindow(window, width=1080, height=720)
    window_register.place(x=0, y=0)
    currentpanel = window_register

    window_register.configure(bg = "#d3d3d3")

    ficheiro_img = os.path.join('imgs\profile_pics', 'avatarnone.png')

    register_img = Canvas(window_register, width=100, height=100, bd=0)
    register_img.place(x=510, y=70)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    lblTitulo = Label(window_register, text = "Registro", fg = "black", bg = "#d3d3d3", font = "arial, 15", relief = "flat")
    lblTitulo.place (x=520, y=25)

    name_register = StringVar()
    label_name = Label(window_register, text="Nome completo:", bg = "#d3d3d3")
    entry_name = Entry(window_register, width=40, textvariable=name_register)
    label_name.place(x=440, y=220)
    entry_name.place(x=440, y=245)

    email_register = StringVar()
    label_email = Label(window_register, text="E-mail:", bg = "#d3d3d3")
    entry_email = Entry(window_register, width=40, textvariable=email_register)
    label_email.place(x=440, y=290)
    entry_email.place(x=440, y=315)

    username_register = StringVar()
    label_username = Label(window_register, text="Nome de usuário:", bg = "#d3d3d3")
    entry_username = Entry(window_register, width=40, textvariable=username_register)
    label_username.place(x=440, y=360)
    entry_username.place(x=440, y=385)

    password_register = StringVar()
    label_password = Label(window_register, text="Password:", bg = "#d3d3d3")
    entry_password = Entry(window_register, width=40, textvariable=password_register, show='*')
    label_password.place(x=440, y=430)
    entry_password.place(x=440, y=455)

    btn_submit_register = Button(window_register, text="Registar", width=34, command= lambda: [submit_register(name_register.get(), email_register.get(), username_register.get(), password_register.get())])
    btn_submit_register.place(x=440, y=510)
    btn_voltar = Button(window_register, text="Voltar", width=34, command=panel_homepage)
    btn_voltar.place(x=440, y=575)

## - - - - - - - - - - CONTAINER LOGIN - - - - - - - - - - ##

def panel_login():
    global currentpanel
    currentpanel.pack_forget()

    window_login = PanedWindow(window, width=1080, height=720)
    currentpanel = window_login

    window_login.configure(bg = "#d3d3d3")

    ficheiro_img = os.path.join('imgs\profile_pics', 'avatarnone.png')

    register_img = Canvas(window_login, width=100, height=100, bd=0, bg = "#d3d3d3")
    register_img.place(x=510, y=70)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    lblTitulo = Label(window_login, text = "Log in", fg = "black", bg = "#d3d3d3", font = "arial, 15", relief = "flat")
    lblTitulo.place (x=530, y=25)

    username_login = StringVar()
    label_username = Label(window_login, text="Nome de usuário:", bg = "#d3d3d3")
    entry_username = Entry(window_login, width=40, textvariable=username_login)
    label_username.place(x=440, y=220)
    entry_username.place(x=440, y=245)

    password_login = StringVar()
    label_password = Label(window_login, text="Password:", bg = "#d3d3d3")
    entry_password = Entry(window_login, width=40, textvariable=password_login, show='*')
    label_password.place(x=440, y=290)
    entry_password.place(x=440, y=315)

    btn_submit_login = Button(window_login, text="Login", width=34, command= lambda: login_and_change_page(username_login.get(), password_login.get(), panel_account))
    btn_submit_login.place(x=440, y=380)

    btn_register = Button(window_login, text="Não tens conta? Registre-se", width=34, command=panel_register)
    btn_register.place(x=440, y=440)

    btn_voltar = Button(window_login, text="Voltar", width=34, command=panel_homepage)
    btn_voltar.place(x=440, y=500)

    window_login.place(x=0, y=0)

## - - - - - - - - - - CONTAINER ACCOUNT - - - - - - - - - - ##

def panel_account():
    global currentpanel
    currentpanel.pack_forget()

    window_account = PanedWindow(window, width=1080, height=720)
    currentpanel = window_account

    window_account.configure(bg = "#d3d3d3")

    name, username, icon, bio, user_id = retrieve_current_user_data()

    ficheiro_img = os.path.join('imgs\\profile_pics', icon)

    register_img = Canvas(window_account, width=100, height=100, bd=0)
    register_img.place(x=100, y=40)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    label_username = Label(window_account, text=name, font=("Helvetica", 24), bg = "#d3d3d3")
    label_username.place(x=220, y=40)

    text_label_username = '@' + username
    label_username = Label(window_account, text=text_label_username, font=("Helvetica", 12), bg = "#d3d3d3")
    label_username.place(x=220, y=90)

    label_username = Label(window_account, text=bio, justify='center', wraplength=240, bg = "#d3d3d3")
    label_username.place(x=100, y=160)

    btn_edit_profile = Button(window_account, text="Editar perfil", width=20, bg = "#d3d3d3", command=panel_edit_profile)
    btn_edit_profile.place(x=800, y=40)

    btn_logout = Button(window_account, text="Fazer logout", width=20, command= lambda: logout_and_change_page(panel_homepage))

    if username == 'admin':
        btn_admin = Button(window_account, text="Painel do administrador", width=20, command=panel_admin)
        btn_admin.place(x=800, y=90)
        btn_logout.place(x=800, y=140)
    else:
        btn_logout.place(x=800, y=90)

    window_account.place(x=0, y=0)


## - - - - - - - - - - CONTAINER DELETE ALBUM - - - - - - - - - - ##

def panel_delete_album():
    global currentpanel
    currentpanel.pack_forget()

    panel_delete_album = PanedWindow(window, width=1080, height=720)
    panel_delete_album.place(x=0,y=0)
    currentpanel = panel_delete_album
    panel_delete_album.configure(bg = "#d3d3d3")

    lblTitulo = Label(panel_delete_album, text = "Delete um álbum", fg = "black", bg = "#d3d3d3", font = "arial, 15", relief = "flat")
    lblTitulo.place (x=60, y=25)

    label_album = Label(panel_delete_album, text="Álbum que deseja apagar: ", bg = "#d3d3d3")
    label_album.place(x=60, y=100)
    del_album = Entry(panel_delete_album, width=30)
    del_album.place(x=60, y=130)

    label_artista = Label(panel_delete_album, text="Artista do álbum que deseja apagar: ", bg = "#d3d3d3")
    label_artista.place(x=60, y=170)
    del_artista = Entry(panel_delete_album, width=30)
    del_artista.place(x=60, y=200)

    btn_delete = Button(panel_delete_album, text="Apagar álbum", width=20, command= lambda: deletar_album(del_album, del_artista))
    btn_delete.place(x=90, y=300)

## - - - - - - - - - CONTAINER ALBUM INFO - - - - - - - - - ##

def panel_album(img, album_name, album_artist, album_info, album_score, album_description):
    global currentpanel
    currentpanel.pack_forget()

    window_album = PanedWindow(window, width=1080, height=720)
    currentpanel = window_album
    
    # img, album_name, album_artist, album_info, album_score, album_description = album_contents(album_id)

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

    # songs = album_songs
    # Label_songs = Label(window_album, text=songs, fg="black")
    # Label_songs.place(x=20,y=350)

    global share_btn
    share_btn= PhotoImage(file="imgs\share-icon.png")
    share_label= Label(image=share_btn)
    button_share= Button(window_album, relief = "raised", image=share_btn, borderwidth=0)
    button_share.place(x = 20, y = 220)

    global like_btn
    like_btn= PhotoImage(file="imgs\heart-icon.png")
    like_label= Label(image=like_btn)
    button_like= Button(window_album, relief = "raised", image=like_btn, borderwidth=0, command=like)
    button_like.place(x = 80, y = 220)

    global stars_btn
    stars_btn= PhotoImage(file="imgs\star-icon.png")
    stars_label= Label(image=stars_btn)
    button_stars= Button(window_album, image=stars_btn, borderwidth=0, command = one_star)
    button_stars.place(x = 250, y = 220)

    global stars_btn2
    stars_btn2= PhotoImage(file="imgs\star-icon.png")
    stars_label2= Label(image=stars_btn2)
    button_stars2= Button(window_album, image=stars_btn2, borderwidth=0, command = two_stars)
    button_stars2.place(x = 285, y = 220)

    global stars_btn3
    stars_btn3= PhotoImage(file="imgs\star-icon.png")
    stars_label3= Label(image=stars_btn3)
    button_stars3= Button(window_album, image=stars_btn3, borderwidth=0, command = three_stars)
    button_stars3.place(x = 320, y = 220)

    global stars_btn4
    stars_btn4= PhotoImage(file="imgs\star-icon.png")
    stars_label4= Label(image=stars_btn4)
    button_stars4= Button(window_album, image=stars_btn4, borderwidth=0, command = four_stars)
    button_stars4.place(x = 355, y = 220)

    global stars_btn5
    stars_btn5= PhotoImage(file="imgs\star-icon.png")
    stars_label5= Label(image=stars_btn5)
    button_stars5= Button(window_album, image=stars_btn5, borderwidth=0, command = five_stars)
    button_stars5.place(x = 390, y = 220)

    btnVoltar = Button(window_album, text="Voltar", width=10, command=panel_homepage)
    btnVoltar.place(x=30, y=500)

    window_album.place(x=0, y=0)

## - - - - - - - - - - CONTAINER ADD ALBUMS - - - - - - - - - - ##

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
    lblQt.place(x=370, y=70)
    qt = IntVar()
    entryQt = Entry(window_adicionar_album, width=25, textvariable=qt)
    entryQt.place(x=450, y= 70) 

    lblDuracao = Label(window_adicionar_album, text = "Duração")
    lblDuracao.place(x=370, y=120)
    duracao = StringVar()
    entryDuracao = Entry(window_adicionar_album, width=25, textvariable=duracao)
    entryDuracao.place(x=450, y= 120) 

    lblMetacritic = Label(window_adicionar_album, text = "Metacritic")
    lblMetacritic.place(x=370, y=170)
    metacritic = IntVar()
    entryMetacritic = Entry(window_adicionar_album, width=25, textvariable=metacritic)
    entryMetacritic.place(x=450, y= 170) 

    lblDescricao = Label(window_adicionar_album, text = "Descrição")
    lblDescricao.place(x=370, y=220)
    descricao = StringVar()
    entryDescricao = Entry(window_adicionar_album, width=25, textvariable=descricao)
    entryDescricao.place(x=450, y= 220) 

    lblMusicas = Label(window_adicionar_album, text = "Músicas")
    lblMusicas.place(x=370, y=270)
    musicas=StringVar()
    entryMusicas = Entry(window_adicionar_album, width=25, textvariable=musicas)
    entryMusicas.place(x=450, y= 270) 

    global image1
    image1 = PhotoImage(file = "imgs\\add.png" )
    btnInserir = Button(window_adicionar_album, image = image1, width=48, height=48, 
                command= lambda: inserir_album(nome.get(), artista.get(), generoalbum.get(), ano.get(), qt.get(), duracao.get(), metacritic.get(), descricao.get(), musicas.get()))
    btnInserir.place(x=400, y= 350)

    window_adicionar_album.place(x=0, y=0)

## - - - - - - - - - - CONTAINER FILTER ALBUMS - - - - - - - - - ##

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
    imagePesq = PhotoImage(file = "imgs\\pesquisar.png")

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

    window_consultar_album.place(x=0,y=0)

## - - - - - - - - - - CONTAINER ADMIN PANEL - - - - - - - - - - ##

def panel_admin():
    global currentpanel
    currentpanel.pack_forget()

    painel_adm = PanedWindow(window, width=1080, height=720)
    painel_adm.place(x=0,y=0)
    currentpanel = painel_adm
    painel_adm.configure(bg = "#d3d3d3")
    
    # imagem
    userImg = PhotoImage(file= "./imgs/painel_adm/user.png")
    labelImg = Label(painel_adm, image=userImg, width=180, height=180, bd=0, bg="#d3d3d3")
    labelImg.place(x= 420, y=100)


    # botão voltar
    btnVoltar = Button(painel_adm, text="Voltar", width=10, command=panel_account)
    btnVoltar.place(x=30, y=30)

    # botão add album
    btnAddAlbum = Button(painel_adm, text="Adicione um álbum", width=25, command=panel_adicionar_albuns)
    btnAddAlbum.place(x=300, y=480)

    # botão remover album
    btnRemovAlbum = Button(painel_adm, text="Remova um álbum", width=25, command=panel_delete_album)
    btnRemovAlbum.place(x=520, y=480)

    # botão usuarios
    btnUsers = Button(painel_adm, text="Veja usuários", width=25)
    btnUsers.place(x=300, y=525)

    # botão apagar reviews
    btnApagarReviews = Button(painel_adm, text="Apague um review", width=25)
    btnApagarReviews.place(x=520, y=525)

    btnFiltrar = Button(painel_adm, text="Filtrar álbuns", width=25, command=panel_filtrar_albuns)
    btnFiltrar.place(x=300, y=565)
    # info user
    name= retrieve_current_user_data()
    username= retrieve_current_user_data()
    icon = retrieve_current_user_data()

    userInfoName = "Nome: " + str(name[0])
    label_userInfoName = Label(painel_adm, text=userInfoName, bg = "#d3d3d3")
    label_userInfoName.place (x=460, y=340)

    userInfoUsername = "Username: " + str(username[1])
    label_userInfoUsername = Label(painel_adm, text=userInfoUsername, bg = "#d3d3d3")
    label_userInfoUsername.place (x=460, y=370)

    admTxt = Label(painel_adm, text="Função: administrador", width=24, bd=0, bg="#d3d3d3", fg="black")
    admTxt.place(x=440, y=400)

    painel_adm.mainloop()



## - - - - - - - - - - CONTAINER NOTIFICACOES - - - - - - - - - - ##

def panel_notific():
    global currentpanel
    currentpanel.pack_forget()

    panel_notific = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_notific
    panel_notific.configure(bg = "#d3d3d3")

    txt = Label(panel_notific, text="Isto é uma notificacao", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
    txt.place(x=420, y=345) 

## - - - - - - - - - - CONTAINER SEARCH - - - - - - - - - - ##

def panel_search():
    global currentpanel
    currentpanel.pack_forget()

    panel_search = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_search
    panel_search.configure(bg = "#d3d3d3")


    txt = Label(panel_notific, text="Pesquise aqui", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
    txt.place(x=420, y=345)



## - - - - - - - - - - CONTAINER HOMEPAGE - - - - - - - - - - ##

def panel_homepage():
    global currentpanel
    currentpanel.pack_forget()

    home_page = PanedWindow(window, width=1080, height=720)
    home_page.place(x=0,y=0)
    currentpanel = home_page
    home_page.configure(bg = "#d3d3d3")

    #coloca título da app
    lblTitulo = Label(home_page, text = "Songsy", fg = "black", bg = "#d3d3d3", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    imgSearch = PhotoImage(file = "./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (home_page, width = 40, height = 40, image = imgSearch, border=0, bg="#d3d3d3", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (home_page, width = 40, height = 40, image = imgUser, border=0, bg="#d3d3d3", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)
    btnGuardarN = Button (home_page, width = 40, height = 40, image = imgNotific, border=0, bg="#d3d3d3", command=panel_notific)
    btnGuardarN.place (x = 930 , y = 9)

    #define area de destaques
    frameDestaques = LabelFrame (home_page, text = "   Álbuns em destaque:   ", width= 800, height=350, bg="#d3d3d3", font="Arial, 10", fg= "black")
    frameDestaques.place (x=140, y=80)

    #define os 3 albuns destacados cada um levando a pagina do album quando clicado
                # !!!    falta colocar o comando pra ir pra pag de cada album    !!!
    imgAlbum1 = PhotoImage(file = "./imgs/home/harrys-house.png", height= 200, width= 200)
    btnGuardarA1 = Button (home_page, width = 200, height = 200, image = imgAlbum1, border=0, bg="#d3d3d3", command=lambda:generate_page_album(2))
    btnGuardarA1.place (x = 190 , y = 135)
    tituloA1 = Label(home_page, text="Harry's House \n by Harry Styles \n POP", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
    tituloA1.place(x=210, y=345)

    imgAlbum2 = PhotoImage(file = "./imgs/home/divine-feminine.png", height= 200, width= 200)
    btnGuardarA2 = Button (home_page, width = 200, height = 200, image = imgAlbum2, border=0, bg="#d3d3d3")   #30px de distancia entre cada album
    btnGuardarA2.place (x = 430 , y = 135)
    tituloA2 = Label(home_page, text="The divine feminine \n by Mac Miller \n HIP-HOP", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
    tituloA2.place(x=450, y=345)

    imgAlbum3 = PhotoImage(file = "./imgs/home/born-pink.png", height= 200, width= 200)
    btnGuardarA3 = Button (home_page, width = 200, height = 200, image = imgAlbum3, border=0, bg="#d3d3d3")   #30px de distancia entre cada album
    btnGuardarA3.place (x = 670 , y = 135)
    tituloA3 = Label(home_page, text="Born Pink \n by BLACKPINK \n K-POP", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
    tituloA3.place(x=690, y=345)


    # mostra os generos musicias suportados pela app
    frameGeneros = LabelFrame (home_page, text = "   Géneros musicais:   ", width= 250, height=110, bg="#d3d3d3", font="Arial, 10", fg= "black")
    frameGeneros.place (x=140, y=470)

    generos = Label(home_page, text="POP \n HIP-HOP \n K-POP", bg="#d3d3d3", fg="black")
    generos.place (x=160, y=500)

    generos2 = Label(home_page, text="ROCK \n R&B \n COUNTRY", bg="#d3d3d3", fg="black")
    generos2.place (x=300, y=500)


    home_page.mainloop()



## - - - - - - - - - - - - - - - - - - - - - - - - - - - ##
## - - - - - - - - - - MAIN CONTAINER - - - - - - - - - - ##

class Application:
    def __init__(self, master=None):
        pass

window = Tk()
Application(window)
window.geometry('1080x720')
window.title('   Songsy')
window.resizable(0,0)
window.iconbitmap("./imgs/home/music.ico")

home_page = PanedWindow(window, width=1080, height=720)
home_page.place(x=0,y=0)
home_page.configure(bg = "#d3d3d3")

#coloca título da app
lblTitulo = Label(home_page, text = "Songsy", fg = "black", bg = "#d3d3d3", font = "Arial, 25",relief = "flat")
lblTitulo.place (x=500, y=5)

#define icone da lupa no botao de busca
imgSearch = PhotoImage(file = "./imgs/home/search.png", height=20, width=20)
btnGuardarS = Button (home_page, width = 40, height = 40, image = imgSearch, border=0, bg="#d3d3d3", command=panel_search)
btnGuardarS.place (x = 1020 , y = 7)

#define icone de user no botao para ir p/ página do usuário
imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
btnGuardarU = Button (home_page, width = 40, height = 40, image = imgUser, border=0, bg="#d3d3d3", command=panel_login)
btnGuardarU.place (x = 975 , y = 9)

#define icone de sino para ir pra página de notificações
imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)
btnGuardarN = Button (home_page, width = 40, height = 40, image = imgNotific, border=0, bg="#d3d3d3", command=panel_notific)
btnGuardarN.place (x = 930 , y = 9)

#define area de destaques
frameDestaques = LabelFrame (home_page, text = "   Álbuns em destaque:   ", width= 800, height=350, bg="#d3d3d3", font="Arial, 10", fg= "black")
frameDestaques.place (x=140, y=80)

#define os 3 albuns destacados cada um levando a pagina do album quando clicado
            # !!!    falta colocar o comando pra ir pra pag de cada album    !!!
imgAlbum1 = PhotoImage(file = "./imgs/home/harrys-house.png", height= 200, width= 200)
btnGuardarA1 = Button (home_page, width = 200, height = 200, image = imgAlbum1, border=0, bg="#d3d3d3", command=lambda:generate_page_album(2))
btnGuardarA1.place (x = 190 , y = 135)
tituloA1 = Label(home_page, text="Harry's House \n by Harry Styles \n POP", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
tituloA1.place(x=210, y=345)

imgAlbum2 = PhotoImage(file = "./imgs/home/divine-feminine.png", height= 200, width= 200)
btnGuardarA2 = Button (home_page, width = 200, height = 200, image = imgAlbum2, border=0, bg="#d3d3d3")   #30px de distancia entre cada album
btnGuardarA2.place (x = 430 , y = 135)
tituloA2 = Label(home_page, text="The divine feminine \n by Mac Miller \n HIP-HOP", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
tituloA2.place(x=450, y=345)

imgAlbum3 = PhotoImage(file = "./imgs/home/born-pink.png", height= 200, width= 200)
btnGuardarA3 = Button (home_page, width = 200, height = 200, image = imgAlbum3, border=0, bg="#d3d3d3")   #30px de distancia entre cada album
btnGuardarA3.place (x = 670 , y = 135)
tituloA3 = Label(home_page, text="Born Pink \n by BLACKPINK \n K-POP", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
tituloA3.place(x=690, y=345)


# mostra os generos musicias suportados pela app
frameGeneros = LabelFrame (home_page, text = "   Géneros musicais:   ", width= 250, height=110, bg="#d3d3d3", font="Arial, 10", fg= "black")
frameGeneros.place (x=140, y=470)

generos = Label(home_page, text="POP \n HIP-HOP \n K-POP", bg="#d3d3d3", fg="black")
generos.place (x=160, y=500)

generos2 = Label(home_page, text="ROCK \n R&B \n COUNTRY", bg="#d3d3d3", fg="black")
generos2.place (x=300, y=500)

currentpanel = home_page

window.mainloop()