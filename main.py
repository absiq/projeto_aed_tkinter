from tkinter import *
from tkinter import ttk
import os
from users import *
from notifications import *
from favoritos import *
from categorias import *
from infoalbum import *
from comentarios import *
from ratings import *
from tkinter import filedialog 
from maisVistos import *

## GUI implementation

#### PAGE SWITCHERS 

def logout_and_change_page(page):
    logout_user()
    page()

def login_and_change_page(username, password, page):
    if submit_login(username, password) == True:
        page()

def generate_page_album(album_id):
    img, album_name, album_artist, album_info, album_score, album_description, alb_id = album_contents(album_id)
    panel_album(img, album_name, album_artist, album_info, album_score, album_description, alb_id)
    
    with open("databases/albums.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        split = line.split(";")
        id = split[0]
        views = int(split[-2])
        if id == album_id:
            views += 1
            split[10] = str(views)
            lines[i] = ";".join(split)
    with open("databases/albums.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)


def login_or_account():
    pasta = '.\\databases'
    ficheiro = '.\\databases\\currentsession.csv'
    verify_files(pasta, ficheiro)
    f = open(ficheiro, 'r')
    campos = f.readlines()
    if campos != []:
        panel_account()
    else:
        panel_login()

#### MISC FUNCTIONS

def like(album_id):
    user_id = retrieve_current_user_id
    likeList(user_id, album_id)
    like_btn['file'] = "imgs\heart-icon-full.png"

def one_star(album_id):
    user_id = retrieve_current_user_id()
    insert_rating(user_id, album_id, '1')
    stars_btn['file'] = "imgs\star-icon-full.png"

def two_stars(album_id):
    user_id = retrieve_current_user_id()
    insert_rating(user_id, album_id, '2')
    stars_btn['file'] = "imgs\star-icon-full.png"
    stars_btn2['file'] = "imgs\star-icon-full.png"

def three_stars(album_id):
    user_id = retrieve_current_user_id()
    insert_rating(user_id, album_id, '3')
    stars_btn['file'] = "imgs\star-icon-full.png"
    stars_btn2['file'] = "imgs\star-icon-full.png"
    stars_btn3['file'] = "imgs\star-icon-full.png"

def four_stars(album_id):
    user_id = retrieve_current_user_id()
    insert_rating(user_id, album_id, '4')
    stars_btn['file'] = "imgs\star-icon-full.png"
    stars_btn2['file'] = "imgs\star-icon-full.png"
    stars_btn3['file'] = "imgs\star-icon-full.png"
    stars_btn4['file'] = "imgs\star-icon-full.png"

def five_stars(album_id):
    user_id = retrieve_current_user_id()
    insert_rating(user_id, album_id, '5')
    stars_btn['file'] = "imgs\star-icon-full.png"
    stars_btn2['file'] = "imgs\star-icon-full.png"
    stars_btn3['file'] = "imgs\star-icon-full.png"
    stars_btn4['file'] = "imgs\star-icon-full.png"
    stars_btn5['file'] = "imgs\star-icon-full.png"

## - - - - - - - - - - PANEL NOTIFICATIONS - - - - - - - - - - ##

panelNot = False

def close_notifications(panel):
    global panelNot
    clear_notifications()
    panelNot = False
    panel.place_forget()

def panel_notifications(event):
    global panelNot
    global currentpanel
    if not panelNot:
        notifications = PanedWindow(window, width=300, height=500)
        notifications.place(x=730, y=60)
        currentpanel = notifications
        panelNot = True

        user_id = retrieve_current_user_id()
        read_notifications(user_id)

        filenotifications = '.\\databases\\currentnotifications.csv'
        f = open(filenotifications, 'r')
        notifications_data = f.readlines()
        notification_counter = 0
        const_x = 5
        new_y = 5
        description_list = []
        for i in notifications_data:
            if i == '\n':
                notification_counter += 0
            else:
                campos = i.split(';')
                title = ' ' + campos[0].replace("'", '') + ' '
                description = campos[1].replace("'", '')
                if title == " 0 ":
                    notification_counter = notification_counter
                else:
                    description_list.insert(notification_counter, description)
                    frameNotification = LabelFrame(notifications, width=280, height=100, text=title)
                    frameNotification.place(x=const_x, y=new_y)
                    new_y += 110
                    notification_counter += 1

        if notification_counter == 1:
            description_0 = Label(notifications, text=description_list[0])
            description_0.place(x=8, y=25)
        elif notification_counter == 2:
            description_0 = Label(notifications, text=description_list[0])
            description_0.place(x=8, y=25)
            description_1 = Label(notifications, text=description_list[1])
            description_1.place(x=8, y=135)
        elif notification_counter == 3:
            description_0 = Label(notifications, text=description_list[0])
            description_0.place(x=8, y=25)
            description_1 = Label(notifications, text=description_list[1])
            description_1.place(x=8, y=135)
            description_2 = Label(notifications, text=description_list[2])
            description_2.place(x=8, y=245)
        elif notification_counter == 4:
            description_0 = Label(notifications, text=description_list[0])
            description_0.place(x=8, y=25)
            description_1 = Label(notifications, text=description_list[1])
            description_1.place(x=8, y=135)
            description_2 = Label(notifications, text=description_list[2])
            description_2.place(x=8, y=245)
            description_3 = Label(notifications, text=description_list[3])
            description_3.place(x=8, y=355)
        elif notification_counter <= 0:
            label_notifications = Label(notifications, text="Ainda não há notificações")
            label_notifications.place(x=80, y=40)

        clear_notifications()
        btnLeave = Button(notifications, text="FECHAR", width=10, command = lambda: close_notifications(notifications))
        btnLeave.place(x=120, y=450)


## - - - - - - - - - - CONTAINER GERIR NOTIFICAÇÕES - - - - - - - - - - ##

def find_user_and_insert_notification(username, title, text):
    user_id = get_user_id(username)
    create_notification(user_id, title, text)

def panel_gerir_notificacoes():
    global currentpanel
    currentpanel.pack_forget()

    window_manage_notifs = PanedWindow(window, width=1080, height=720)
    currentpanel = window_manage_notifs
    window_manage_notifs.configure(bg="#121212")

    btn_voltar = Button(window_manage_notifs, text="Voltar", width=20, command=panel_admin)
    btn_voltar.place(x=20, y=20)

    label_username = Label(window_manage_notifs, text="Escreva o username do usuário que deseja enviar uma notificação:", bg="#121212", fg="white")
    label_username.place(x=400, y=40)

    username = StringVar()
    entryUsername = Entry(window_manage_notifs, width=25, textvariable=username)
    entryUsername.place(x=400, y=90) 

    label_title = Label(window_manage_notifs, text="Insira o título da notificação:", bg="#121212", fg="white")
    label_title.place(x=400, y=140)

    label_text = Label(window_manage_notifs, text="Insira o texto da notificação:", bg="#121212", fg="white")
    label_text.place(x=400, y=240)

    notifTitle = StringVar()
    entryTitle = Entry(window_manage_notifs, width=20, textvariable=notifTitle)
    entryTitle.place(x=400, y=190)

    notifText = StringVar()
    entryText = Entry(window_manage_notifs, width=50, textvariable=notifText)
    entryText.place(x=400, y=290)

    btn_send = Button(window_manage_notifs, text="Enviar", width=34, command=lambda:find_user_and_insert_notification(username.get(), notifTitle.get(), notifText.get()))
    btn_send.place(x=440, y=350)

    window_manage_notifs.place(x=0, y=0)

## - - - - - - - - - - CONTAINER EDIT - - - - - - - - - - ##

def panel_edit_profile():
    global currentpanel
    currentpanel.pack_forget()

    window_edit_profile = PanedWindow(window, width=1080, height=720)
    currentpanel = window_edit_profile

    window_edit_profile.configure(bg="#121212")

    name, username, icon, bio, user_id, categoria = retrieve_current_user_data()


    name_text = "O seu nome atual é: " + name
    label_name = Label(window_edit_profile, text=name_text, bg="#121212", fg="white")
    label_name.place(x=20, y=50)

    username_text = "O seu username atual é: " + username
    label_username = Label(window_edit_profile, text=username_text, bg="#121212", fg="white")
    label_username.place(x=400, y=50)

    bio_text = "O sua bio atual é: "
    label_bio_text = Label(window_edit_profile, text=bio_text, bg="#121212", fg="white")
    label_bio = Label(window_edit_profile, justify='center', wraplength=240, text=bio, bg="#121212", fg="white")
    label_bio_text.place(x=20, y=220)
    label_bio.place(x=20, y=240)

    icon_text = "O seu icon atual é: "
    label_icon_text = Label(window_edit_profile, text=icon_text, bg="#121212", fg="white")
    label_icon_text.place(x=740, y=50)

    def seleciona_foto_perfil():
        global cover
        global filename
        filename = filedialog.askopenfilename(title = "Select Image", initialdir="./imgs/profile_pics", filetypes=(("png files", "*.png"), ("all files", "*.*"))) 
        cover = PhotoImage(file = filename)
        canvasImage.itemconfig(image_id, image = cover)
        return filename

    canvasImage = Canvas(window_edit_profile, width = 100, height = 100, bd = 2, relief = "sunken")
    canvasImage.place(x=740, y=80)
    global imagem
    imagem = PhotoImage(file = "imgs\\profile_pics\\avatarnone.png")
    image_id = canvasImage.create_image(50, 50, image=imagem)
    
    btnSelect = Button(window_edit_profile, text= "Selecionar imagem", width=14, height=1, command=seleciona_foto_perfil)
    btnSelect.place(x=740, y=200)
   

    label_new_name = Label(window_edit_profile, text="Insira o seu novo nome:", bg="#121212", fg="white")
    label_new_name.place(x=20, y=80)
    new_name = name
    entry_new_name = Entry(window_edit_profile, width=30, textvariable=new_name)
    entry_new_name.place(x=20, y=100)

    label_new_username = Label(window_edit_profile, text="Insira o seu novo username:", bg="#121212", fg="white")
    label_new_username.place(x=400, y=80)
    new_username = username
    entry_new_username = Entry(window_edit_profile, width=30, textvariable=new_username)
    entry_new_username.place(x=400, y=100)

    label_new_bio = Label(window_edit_profile, text="Insira a sua nova bio:", bg="#121212", fg="white")
    label_new_bio.place(x=20, y=290)
    entry_new_bio = Text(window_edit_profile) # usar GET para inserir conteúdo do Text em new_bio
    entry_new_bio.place(x=20, y=310, width=300, height=100)

    categoria_text = "O seu gênero favorito é: " + categoria
    label_categoria = Label(window_edit_profile, text=categoria_text, bg="#121212", fg="white")
    label_categoria.place(x=400, y=220)
    label_new_fav = Label(window_edit_profile, text="Insira o seu novo gênero favorito:", bg="#121212", fg="white")
    label_new_fav.place(x=400, y=290)

    current_var = StringVar()
    combobox = ttk.Combobox(window_edit_profile, textvariable=current_var)
    categorias = preencheCombobox()
    combobox['values'] = categorias
    combobox['state'] = 'readonly'
    combobox.place(x=400, y=320)

    btn_editar = Button(window_edit_profile, width = 14, height=1, text='Guardar', command=lambda: edit_user_data(entry_new_name.get(), entry_new_username.get(), entry_new_bio.get("1.0",'end-1c'), current_var.get(), filename))
    btn_editar.place(x=740, y=320)

    global imgMusicas
    imgMusicas = PhotoImage(file= "./imgs/painel_account/notas_musicais.png")
    labelImg = Label(window_edit_profile, image=imgMusicas, width=1080, height=300, bg="#121212")
    labelImg.place(x=0, y=550)

    btn_voltar = Button(window_edit_profile, width = 14, height=1, text="Voltar", command=panel_account)
    btn_voltar.place(x=740, y=370)

    window_edit_profile.place(x=0, y=0)


# - - - - - - - - - - CONTAINER REGISTER - - - - - - - - - - #

def create_register(nome, email, username, password):
    submit_register(nome, email, username, password)
    user_id = get_user_id(username)
    insert_new_user_into_notification_database(int(user_id))
    insert_new_user_into_favs_database(int(user_id))

def panel_register():
    global currentpanel
    currentpanel.pack_forget()

    window_register = PanedWindow(window, width=1080, height=720)
    window_register.place(x=0, y=0)
    currentpanel = window_register

    window_register.configure(bg="#121212")

    ficheiro_img = os.path.join('imgs\profile_pics', 'avatarnone.png')

    register_img = Canvas(window_register, width=100, height=100, bd=0)
    register_img.place(x=510, y=70)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    lblTitulo = Label(window_register, text = "Registro", bg="#121212", fg="white", font = "arial, 15", relief = "flat")
    lblTitulo.place (x=520, y=25)

    name_register = StringVar()
    label_name = Label(window_register, text="Nome completo:", bg="#121212", fg="white")
    entry_name = Entry(window_register, width=40, textvariable=name_register)
    label_name.place(x=440, y=220)
    entry_name.place(x=440, y=245)

    email_register = StringVar()
    label_email = Label(window_register, text="E-mail:", bg="#121212", fg="white")
    entry_email = Entry(window_register, width=40, textvariable=email_register)
    label_email.place(x=440, y=290)
    entry_email.place(x=440, y=315)

    username_register = StringVar()
    label_username = Label(window_register, text="Nome de usuário:", bg="#121212", fg="white")
    entry_username = Entry(window_register, width=40, textvariable=username_register)
    label_username.place(x=440, y=360)
    entry_username.place(x=440, y=385)

    password_register = StringVar()
    label_password = Label(window_register, text="Password:", bg="#121212", fg="white")
    entry_password = Entry(window_register, width=40, textvariable=password_register, show='*')
    label_password.place(x=440, y=430)
    entry_password.place(x=440, y=455)

    btn_submit_register = Button(window_register, text="Registar", width=34, command= lambda: create_register(name_register.get(), email_register.get(), username_register.get(), password_register.get()))
    btn_submit_register.place(x=440, y=510)
    btn_voltar = Button(window_register, text="Voltar", width=34, command=panel_homepage)
    btn_voltar.place(x=440, y=575)

    global imgBolinhas1
    imgBolinhas1 = PhotoImage(file= "./imgs/painel_login/notas_musicais_bolinhas.png")
    labelImg1 = Label(window_register, image=imgBolinhas1, width=300, height=600, bg="#121212")
    labelImg1.place(x=6, y=50)
    
    global imgBolinhas2
    imgBolinhas2 = PhotoImage(file= "./imgs/painel_login/notas_musicais_bolinhas.png")
    labelImg2 = Label(window_register, image=imgBolinhas2, width=300, height=600, bg="#121212")
    labelImg2.place(x=770, y=50)

## - - - - - - - - - - CONTAINER LOGIN - - - - - - - - - - ##

def panel_login():
    global currentpanel
    currentpanel.pack_forget()

    window_login = PanedWindow(window, width=1080, height=720)
    currentpanel = window_login

    window_login.configure(bg="#121212")

    ficheiro_img = os.path.join('imgs\profile_pics', 'avatarnone.png')

    register_img = Canvas(window_login, width=100, height=100, bd=0, bg="#121212")
    register_img.place(x=510, y=70)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    lblTitulo = Label(window_login, text = "Log in", bg="#121212", fg="white", font = "arial, 15", relief = "flat")
    lblTitulo.place (x=530, y=25)

    username_login = StringVar()
    label_username = Label(window_login, text="Nome de usuário:", bg="#121212", fg="white")
    entry_username = Entry(window_login, width=40, textvariable=username_login)
    label_username.place(x=440, y=220)
    entry_username.place(x=440, y=245)

    password_login = StringVar()
    label_password = Label(window_login, text="Password:", bg="#121212", fg="white")
    entry_password = Entry(window_login, width=40, textvariable=password_login, show='*')
    label_password.place(x=440, y=290)
    entry_password.place(x=440, y=315)

    btn_submit_login = Button(window_login, text="Login", width=34, command= lambda: login_and_change_page(username_login.get(), password_login.get(), panel_account))
    btn_submit_login.place(x=440, y=380)

    btn_register = Button(window_login, text="Não tens conta? Registre-se", width=34, command=panel_register)
    btn_register.place(x=440, y=440)

    btn_voltar = Button(window_login, text="Voltar", width=34, command=panel_homepage)
    btn_voltar.place(x=440, y=500)
    
    global imgBolinhas1
    imgBolinhas1 = PhotoImage(file= "./imgs/painel_login/notas_musicais_bolinhas.png")
    labelImg1 = Label(window_login, image=imgBolinhas1, width=300, height=600, bg="#121212")
    labelImg1.place(x=6, y=50)
    
    global imgBolinhas2
    imgBolinhas2 = PhotoImage(file= "./imgs/painel_login/notas_musicais_bolinhas.png")
    labelImg2 = Label(window_login, image=imgBolinhas2, width=300, height=600, bg="#121212")
    labelImg2.place(x=770, y=50)
    
    window_login.place(x=0, y=0)

## - - - - - - - - - - CONTAINER ACCOUNT - - - - - - - - - - ##

def panel_account():
    global currentpanel
    currentpanel.pack_forget()

    window_account = PanedWindow(window, width=1080, height=720)
    currentpanel = window_account

    window_account.configure(bg="#121212")

    name, username, icon, bio, user_id, categoria = retrieve_current_user_data()

    ficheiro_img = os.path.join('imgs\\profile_pics', icon)

    register_img = Canvas(window_account, width=100, height=100, bd=0)
    register_img.place(x=100, y=40)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    label_username = Label(window_account, text=name, font=("Helvetica", 24), bg="#121212", fg="white")
    label_username.place(x=220, y=40)

    text_label_username = '@' + username
    label_username = Label(window_account, text=text_label_username, font=("Helvetica", 12), bg="#121212", fg="white")
    label_username.place(x=220, y=90)

    label_bio = Label(window_account, text=bio, justify='center', wraplength=240, bg="#121212", fg="white")
    label_bio.place(x=100, y=160)

    btn_edit_profile = Button(window_account, text="Editar perfil", width=20, command=panel_edit_profile)
    btn_edit_profile.place(x=800, y=40)

    btn_logout = Button(window_account, text="Fazer logout", width=20, command= lambda: logout_and_change_page(panel_homepage))

    global imgMusicas
    imgMusicas = PhotoImage(file= "./imgs/painel_account/notas_musicais.png")
    labelImg = Label(window_account, image=imgMusicas, width=1080, height=300, bg="#121212")
    labelImg.place(x=0, y=550)

    if username == 'admin':
        btn_admin = Button(window_account, text="Painel do administrador", width=20, command=panel_admin)
        btn_admin.place(x=800, y=90)
        btn_logout.place(x=800, y=140)
        btn_voltar = Button(window_account, text="Voltar", width=20, command=panel_homepage)
        btn_voltar.place(x=800, y=190)
    else:
        btn_logout.place(x=800, y=90)
        btn_voltar = Button(window_account, text="Voltar", width=20, command=panel_homepage)
        btn_voltar.place(x=800, y=140)

    label_favoritos = Label(window_account, text='Os seus favoritos', justify='center', wraplength=240, bg="#121212", fg="white")
    label_favoritos.place(x=100, y=240)
    lboxFavoritos=Listbox(window_account, width = 35, height=16, selectmode = "single", relief="flat")
    lboxFavoritos.place(x=100,y=260)
    lboxFavoritos.configure(bg="#121212", fg="white", selectbackground="#1db954")

    user_id = retrieve_current_user_id()
    ficheiro = '.\\databases\\favoritos.csv'
    f = open(ficheiro, 'r')
    dados = f.readlines()
    for line in dados:
        user = line.split(';')
        if user[0] == user_id:
            songs = user[1].split(',')
            for song in songs:
                lboxFavoritos.insert('end', song)


    window_account.place(x=0, y=0)


## - - - - - - - - - - CONTAINER DELETE ALBUM - - - - - - - - - - ##

def panel_delete_album():
    global currentpanel
    currentpanel.pack_forget()

    panel_delete_album = PanedWindow(window, width=1080, height=720)
    panel_delete_album.place(x=0,y=0)
    currentpanel = panel_delete_album
    panel_delete_album.configure(bg="#121212")

    lblTitulo = Label(panel_delete_album, text = "Delete um álbum", bg="#121212", fg="white", font = "arial, 15", relief = "flat")
    lblTitulo.place (x=450, y=45)

    label_album = Label(panel_delete_album, text="Álbum que deseja apagar: ", bg="#121212", fg="white")
    label_album.place(x=450, y=120)
    del_album = Entry(panel_delete_album, width=30)
    del_album.place(x=450, y=150)

    label_artista = Label(panel_delete_album, text="Artista do álbum que deseja apagar: ", bg="#121212", fg="white")
    label_artista.place(x=450, y=190)
    del_artista = Entry(panel_delete_album, width=30)
    del_artista.place(x=450, y=220)

    btn_delete = Button(panel_delete_album, text="Apagar álbum", width=20, command= lambda: deletar_album(del_album, del_artista))
    btn_voltar = Button(panel_delete_album, text="Voltar", width=20, command=panel_admin)
    btn_voltar.place(x=20, y=20)
    btn_delete.place(x=450, y=280)

    global imgMusicas
    imgMusicas = PhotoImage(file= "./imgs/painel_account/notas_musicais.png")
    labelImg = Label(panel_delete_album, image=imgMusicas, width=1080, height=300, bg="#121212")
    labelImg.place(x=0, y=550)


## - - - - - - - - - - CONTAINER COMENTARIOS - - - - - - - - - - ##

def panel_comentarios(album_id):
    global currentpanel
    currentpanel.pack_forget()

    window_comentarios = PanedWindow(window, width=1080, height=720)
    window_comentarios.configure(bg = "#121212")

    img, album_name, album_artist, album_info, album_score, album_description, alb_id = album_contents(album_id)
    lista_comentarios = leitura_comentarios(alb_id)

    page_text = 'Comentários em ' + album_name
    label_page = Label(text=page_text, bg = "#121212", fg = "white", font=('Arial', 14))
    label_page.place(x=10, y=10)

    comments_textarea = Text(window, width=80, height=30)
    comments_textarea.configure(bg = "#121212", fg="white")

    for comment in lista_comentarios:
        comments_textarea.insert(INSERT, comment)

    comments_textarea.place(x=10, y=60)

    btn_voltar = Button(text='Voltar', width=20, command=lambda:generate_page_album(album_id))
    btn_voltar.place(x=920, y=10)

    window_comentarios.place(x=0, y=0)

    

## - - - - - - - - - CONTAINER ALBUM INFO - - - - - - - - - ##

def comment(comment, album_id):
    user_id = retrieve_current_user_id
    inserir_comentario(user_id, comment, album_id)

def panel_album(img, album_name, album_artist, album_info, album_score, album_description, alb_id):
    global currentpanel
    currentpanel.pack_forget()

    update_media(alb_id)

    window_album = PanedWindow(window, width=1080, height=720)
    window_album.configure(bg = "#121212")
    currentpanel = window_album
    
    global cover
    ctn_cover = Canvas(window_album, width=190, height=190, bd=2, bg="#121212", highlightbackground="#121212", relief="sunken")
    ctn_cover.place(x=20, y=20)
    cover = PhotoImage(file = img)
    ctn_cover.create_image(100, 100, image = cover) 

    name = album_name
    Label_name = Label(window_album, text=name, fg="white", bg="#121212", font=('Arial', 80))
    Label_name.place(x=242,y=60)

    artist = album_artist
    Label_artist = Label(window_album, text=artist, fg="white", bg="#121212")
    Label_artist.place(x=250,y=170)
    
    info = album_info
    Label_info = Label(window_album, text=info, fg="white", bg="#121212")
    Label_info.place(x=250,y=199)

    score = album_score
    Label_score = Label(window_album, text=score, fg="white", font=('Arial', 20))
    Label_score.place(x=170, y=220)
    
    scoreMin = 40
    scoreMax = 60
    if int(score) <= scoreMin:
        Label_score.configure(bg="red")
    elif int(score) >= scoreMin and int(score) <= scoreMax:
        Label_score.configure(bg="#cccc00")
    else:
        Label_score.configure(bg="green")

    description = album_description
    Label_description = Label(window_album, text=description, fg="white", bg="#121212", wraplength=660, justify="left")
    Label_description.place(x = 20, y = 270)

    global lboxMusicas
    lboxMusicas=Listbox(window_album, width = 35, height=16, bd="0", selectmode = "single", relief="flat", selectbackground="#1db954", bg="#121212", highlightbackground = "#121212")
    lboxMusicas.place(x=20, y= 360)
    lboxMusicas.configure(foreground="white")
    musicas = "databases\musicas.txt"

    file = open(musicas, "r", encoding="utf-8")
    music = file.readlines()
    file.close()

    for musica in music:
        campos = musica.split(";")
        if campos[0] == str(alb_id):
            for songs in campos[1:]:
                lboxMusicas.insert("end", songs)

    global playBtn
    playBtn = PhotoImage(file="imgs\play_icon.png")
    play_button = Button(window_album, image=playBtn, relief="flat", bd="0", command= lambda: (play_song(lboxMusicas, alb_id)))
    play_button.place(x=80, y= 620)
    play_button.configure(bg="#121212", fg="#121212")

    global pauseBtn
    pauseBtn = PhotoImage(file="imgs\pause_icon.png")
    pause_button = Button(window_album, image=pauseBtn, relief="flat", bd="0", command=pause_song)
    pause_button.place(x=120, y= 620)
    pause_button.configure(bg="#121212", fg="#121212")

    global share_btn
    share_btn= PhotoImage(file="imgs\share-icon.png")
    share_label= Label(image=share_btn)
    button_share= Button(window_album, relief = "raised", image=share_btn, borderwidth=0)
    button_share.place(x = 20, y = 220)
    button_share.configure(bg="#121212", fg="#121212")

    # user_id = retrieve_current_user_id()

    global like_btn
    like_btn= PhotoImage(file="imgs\heart-icon.png")
    like_label= Label(image=like_btn)
    button_like= Button(window_album, relief = "raised", image=like_btn, borderwidth=0, command= lambda: like(alb_id))
    button_like.place(x = 80, y = 220)
    button_like.configure(bg="#121212", fg="#121212")


    global stars_btn
    stars_btn= PhotoImage(file="imgs\star-icon.png")
    stars_label= Label(image=stars_btn)
    button_stars= Button(window_album, image=stars_btn, borderwidth=0, command = lambda: one_star(alb_id))
    button_stars.place(x = 250, y = 220)
    button_stars.configure(bg="#121212", fg="#121212")

    global stars_btn2
    stars_btn2= PhotoImage(file="imgs\star-icon.png")
    stars_label2= Label(image=stars_btn2)
    button_stars2= Button(window_album, image=stars_btn2, borderwidth=0, command = lambda: two_stars(alb_id))
    button_stars2.place(x = 285, y = 220)
    button_stars2.configure(bg="#121212", fg="#121212")

    global stars_btn3
    stars_btn3= PhotoImage(file="imgs\star-icon.png")
    stars_label3= Label(image=stars_btn3)
    button_stars3= Button(window_album, image=stars_btn3, borderwidth=0, command = lambda: three_stars(alb_id))
    button_stars3.place(x = 320, y = 220)
    button_stars3.configure(bg="#121212", fg="#121212")

    global stars_btn4
    stars_btn4= PhotoImage(file="imgs\star-icon.png")
    stars_label4= Label(image=stars_btn4)
    button_stars4= Button(window_album, image=stars_btn4, borderwidth=0, command = lambda: four_stars(alb_id))
    button_stars4.place(x = 355, y = 220)
    button_stars4.configure(bg="#121212", fg="#121212")

    global stars_btn5
    stars_btn5= PhotoImage(file="imgs\star-icon.png")
    stars_label5= Label(image=stars_btn5)
    button_stars5= Button(window_album, image=stars_btn5, borderwidth=0, command = lambda: five_stars(alb_id))
    button_stars5.place(x = 390, y = 220)
    button_stars5.configure(bg="#121212", fg="#121212")

    btnVoltar = Button(window_album, text="Voltar", width=20, command=panel_homepage)
    btnVoltar.place(x=900, y=10)

    comment_frame = Frame(window_album, width=400, height=200, bg="#121212")
    comment_frame.place(x=600, y=360)
    comment_label = Label(comment_frame, text="Comentário:", bg="#121212", fg="white")
    comment_label.place(x = 10, y = 10)
    comment_entry = Text(comment_frame, width=30, height=6)
    comment_entry.place(x = 90, y = 10)
    btn_comentar = Button(comment_frame, text="Comentar", command=lambda:comment(comment_entry.get("1.0",'end-1c'), alb_id))
    btn_comentar.place(x=90, y=150)
    btn_comentarios = Button(comment_frame, text="Ver comentários", command=lambda:panel_comentarios(alb_id))
    btn_comentarios.place(x=180, y=150)

    window_album.place(x=0, y=0)


## - - - - - - - - - - CONTAINER ADD ALBUMS - - - - - - - - - - ##

def add_album(nome, artista, genero, ano, qt, duracao, metacritic, descricao, musicas):
    # função que envia notificação
    users = get_users_by_gender(genero)
    send_notification(users, nome, artista)
    inserir_album(nome, artista, filename, genero, ano, qt, duracao, metacritic, descricao, musicas)

def panel_adicionar_albuns():
    global currentpanel
    currentpanel.pack_forget()

    window_adicionar_album = PanedWindow(window, width=1080, height=720)
    currentpanel = window_adicionar_album
    window_adicionar_album.configure(bg="#121212")

    lblNome = Label(window_adicionar_album, text = "Nome", bg="#121212", fg="white")
    lblNome.place(x=70, y=70)
    nome = StringVar()
    entryNome = Entry(window_adicionar_album, width=25, textvariable=nome)
    entryNome.place(x=150, y= 70) 

    lblArtista = Label(window_adicionar_album, text = "Artista",bg="#121212", fg="white")
    lblArtista.place(x=70, y=120)
    artista = StringVar()
    entryArtista = Entry(window_adicionar_album, width=25, textvariable=artista)
    entryArtista.place(x=150, y= 120) 

    lblAno = Label(window_adicionar_album, text = "Ano",bg="#121212", fg="white")
    lblAno.place(x=70, y=170)
    ano = IntVar()
    entryAno = Entry(window_adicionar_album, width=25, textvariable=ano)
    entryAno.place(x=150, y= 170) 


    lblGenero = Label(window_adicionar_album, text = "Género",bg="#121212", fg="white")
    lblGenero.place(x=70, y=220)
    current_var = StringVar()
    combobox = ttk.Combobox(window_adicionar_album, width = 22, textvariable=current_var)
    categorias = preencheCombobox()
    combobox['values'] = categorias
    combobox['state'] = 'readonly'
    combobox.place(x=150, y=220)


    lblQt = Label(window_adicionar_album, text = "Qt músicas",bg="#121212", fg="white")
    lblQt.place(x=70, y=270)
    qt = IntVar()
    entryQt = Entry(window_adicionar_album, width=25, textvariable=qt)
    entryQt.place(x=150, y= 270) 

    lblDuracao = Label(window_adicionar_album, text = "Duração",bg="#121212", fg="white")
    lblDuracao.place(x=370, y=70)
    duracao = StringVar()
    entryDuracao = Entry(window_adicionar_album, width=25, textvariable=duracao)
    entryDuracao.place(x=450, y= 70) 

    lblMetacritic = Label(window_adicionar_album, text = "Metacritic", bg="#121212", fg="white")
    lblMetacritic.place(x=370, y=120)
    metacritic = IntVar()
    entryMetacritic = Entry(window_adicionar_album, width=25, textvariable=metacritic)
    entryMetacritic.place(x=450, y= 120) 

    lblDescricao = Label(window_adicionar_album, text = "Descrição", bg="#121212", fg="white")
    lblDescricao.place(x=370, y=170)
    descricao = StringVar()
    entryDescricao = Entry(window_adicionar_album, width=25, textvariable=descricao)
    entryDescricao.place(x=450, y= 170) 

    lblMusicas = Label(window_adicionar_album, text = "Músicas", bg="#121212", fg="white")
    lblMusicas.place(x=370, y=220)
    musicas=StringVar()
    entryMusicas = Entry(window_adicionar_album, width=25, textvariable=musicas)
    entryMusicas.place(x=450, y= 220) 

    def selecionaFicheiro():
        global cover
        global filename
        filename = filedialog.askopenfilename(title = "Select Image", initialdir="./imgs/covers", filetypes=(("png files", "*.png"), ("all files", "*.*"))) 
        cover = PhotoImage(file = filename)
        canvasImage.itemconfig(image_id, image = cover)
        return filename

    canvasImage = Canvas(window_adicionar_album, width = 200, height = 200, bd = 2, relief = "sunken")
    canvasImage.place(x=650, y=70)
    global imagem
    imagem = PhotoImage(file = "imgs\covers\\No_Image.png")
    image_id = canvasImage.create_image(100, 100, image=imagem)
    
    btnSelect = Button(window_adicionar_album, text= "Selecionar Imagem", width=28, height=1, command=selecionaFicheiro)
    btnSelect.place(x=650, y=280)

    global image1
    image1 = PhotoImage(file = "imgs\\add.png" )
    btnInserir = Button(window_adicionar_album, image = image1, width=48, height=48, 
                command= lambda: add_album(nome.get(), artista.get(), current_var.get(), ano.get(), qt.get(), duracao.get(), metacritic.get(), descricao.get(), musicas.get()))
    btnInserir.place(x=650, y= 350)

    btn_voltar = Button(window_adicionar_album, text="Voltar", width=20, command=panel_admin)
    btn_voltar.place(x=20, y=20)

    global imgMusicas
    imgMusicas = PhotoImage(file= "./imgs/painel_account/notas_musicais.png")
    labelImg = Label(window_adicionar_album, image=imgMusicas, width=1080, height=300, bg="#121212")
    labelImg.place(x=0, y=550)

    window_adicionar_album.place(x=0, y=0)

## - - - - - - - - - - CONTAINER GERENCIAR CATEGORIAS - - - - - - - - - ##

def preencheCombobox():
    """
    função que irá preencher a combobox com as categorias
    """
    ficheiroCategorias = 'databases/categorias.txt'
    f = open(ficheiroCategorias, "r", encoding="utf-8")
    categorias = f.readlines()
    f.close()
    return categorias

def panel_categorias():
    """
    Painel de gerenciamento de categorias
    """
    global currentpanel
    currentpanel.pack_forget()

    window_consultar_categorias = PanedWindow(window, width=1080, height=720)
    window_consultar_categorias.configure(bg = "#121212")
    currentpanel = window_consultar_categorias

    btn_voltar = Button(window_consultar_categorias, text="Voltar", width = 20, command=panel_admin)
    btn_voltar.place(x=20, y=20)

    label_remover = Label(window_consultar_categorias, fg = "white", bg = "#121212", text="Remover uma categoria:")
    label_remover.place(x=100, y=90)

    current_var = StringVar()
    combobox = ttk.Combobox(window_consultar_categorias, textvariable=current_var)
    categorias = preencheCombobox()
    combobox['values'] = categorias
    combobox['state'] = 'readonly'
    combobox.place(x=100, y=150)

    btn_remover = Button(window_consultar_categorias, text="Remover", command=lambda:remover_categoria(current_var.get()))
    btn_remover.place(x=260, y=150)

    label_adicionar = Label(window_consultar_categorias, fg = "white", bg = "#121212", text="Adicionar uma categoria:")
    label_adicionar.place(x=100, y=260)

    current_input = StringVar()
    entry_categoria = Entry(window_consultar_categorias, textvariable=current_input)
    entry_categoria.place(x=100, y=320)

    btn_add = Button(window_consultar_categorias, text="Adicionar", command=lambda:inserir_categoria(current_input.get()))
    btn_add.place(x=260, y=320)

    columns = ('categorias')
    treeview = ttk.Treeview(window_consultar_categorias, selectmode="browse", columns=columns, show='headings')
    treeview.heading('categorias', text='Categorias')
    for categoria in categorias:
        treeview.insert('', END, values=categoria)
    treeview.place(x=500, y=90)
    window_consultar_categorias.place(x=0, y=0)
    btn_refresh = Button(window_consultar_categorias, text="Refresh", command=panel_categorias)
    btn_refresh.place(x=580, y=320)

    global imgMusicas
    imgMusicas = PhotoImage(file= "./imgs/painel_account/notas_musicais.png")
    labelImg = Label(window_consultar_categorias, image=imgMusicas, width=1080, height=300, bg="#121212")
    labelImg.place(x=0, y=550)


## - - - - - - - - - - CONTAINER FILTER ALBUMS - - - - - - - - - ##

def panel_filtrar_albuns():
    """
    Painel de consulta com filtros
    """

    global currentpanel
    currentpanel.pack_forget()

    window_consultar_album = PanedWindow(window, width=1080, height=720)
    currentpanel = window_consultar_album
    window_consultar_album.configure(bg="#121212")

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
    choice7 = IntVar()
    choice7.set(0) 

    ck1 = Checkbutton(window_consultar_album, text = "POP", variable = choice1)
    ck2 = Checkbutton(window_consultar_album, text = "K-POP", variable = choice2)
    ck3 = Checkbutton(window_consultar_album, text = "HIP-HOP", variable = choice3)
    ck4 = Checkbutton(window_consultar_album, text = "ROCK", variable = choice4)
    ck5 = Checkbutton(window_consultar_album, text = "R&B", variable = choice5)
    ck6 = Checkbutton(window_consultar_album, text = "COUNTRY", variable = choice6)
    ck7 = Checkbutton(window_consultar_album, text = "OUTROS", variable = choice7)
    ck1.place(x=150, y=70)
    ck2.place(x=250, y=70)
    ck3.place(x=350, y=70)
    ck4.place(x=450, y=70)
    ck5.place(x=550, y=70)
    ck6.place(x=650, y=70)
    ck7.place(x=750, y=70)


    global imagePesq
    imagePesq = PhotoImage(file = "imgs\\pesquisar.png")

    btnPesquisar = Button(window_consultar_album, width=48, height=48, image = imagePesq, 
            command = lambda: filtrar_albuns(tree, choice1, choice2, choice3, choice4, choice5, choice6, choice7, num_albuns))
    btnPesquisar.place(x=850, y= 50)

    tree = ttk.Treeview(window_consultar_album, columns = ("Nome", "Artista", "Género", "Ano"), show = "headings", height = 12, selectmode = "browse")
    tree.column("Nome", width = 220, anchor = "w")
    tree.column("Artista", width = 100, anchor = "c")
    tree.column("Género", width = 220, anchor = "c")
    tree.column("Ano", width = 220, anchor = "c")

    tree.heading("Nome", text = "Nome")
    tree.heading("Artista", text = "Artista")
    tree.heading("Género", text = "Género")
    tree.heading("Ano", text = "Ano")
    tree.place(x=150, y=110)

      
    lbl_num_albuns = Label(window_consultar_album, text = "Nº de álbuns", font = ("Helvetica", "10"), bg="#121212", fg="white")
    lbl_num_albuns.place(x=150, y=390)

    num_albuns = StringVar()
    txt_num_albuns = Entry(window_consultar_album, width=10, textvariable = num_albuns)
    txt_num_albuns.place(x=240, y=390)

    btn_voltar = Button(window_consultar_album, text="Voltar", width=20, command=panel_admin)
    btn_voltar.place(x=20, y=20)

    global imgMusicas
    imgMusicas = PhotoImage(file= "./imgs/painel_account/notas_musicais.png")
    labelImg = Label(window_consultar_album, image=imgMusicas, width=1080, height=300, bg="#121212")
    labelImg.place(x=0, y=550)

    window_consultar_album.place(x=0,y=0)

## - - - - - - - - - - CONTAINER ADMIN PANEL - - - - - - - - - - ##

def panel_admin():
    global currentpanel
    currentpanel.pack_forget()

    painel_adm = PanedWindow(window, width=1080, height=720)
    painel_adm.place(x=0,y=0)
    currentpanel = painel_adm
    painel_adm.configure(bg="#121212")
    
    # imagem
    userImg = PhotoImage(file= "./imgs/painel_adm/user.png")
    labelImg = Label(painel_adm, image=userImg, width=180, height=180, bd=0, bg="#121212", fg="white")
    labelImg.place(x= 420, y=100)


    # botão voltar
    btnVoltar = Button(painel_adm, text="Voltar", width=20, command=panel_account)
    btnVoltar.place(x=20, y=20)

    # botão add album
    btnAddAlbum = Button(painel_adm, text="Adicione um álbum", width=25, command=panel_adicionar_albuns)
    btnAddAlbum.place(x=300, y=480)

    # botão remover album
    btnRemovAlbum = Button(painel_adm, text="Remova um álbum", width=25, command=panel_delete_album)
    btnRemovAlbum.place(x=520, y=480)

    # botão usuarios
    btnUsers = Button(painel_adm, text="Veja usuários", width=25)
    btnUsers.place(x=300, y=525)

    # botão filtrar álbuns
    btnFiltrar = Button(painel_adm, text="Filtrar álbuns", width=25, command=panel_filtrar_albuns)
    btnFiltrar.place(x=300, y=570)

    # botão gerenciar categorias
    btnGerenciarCategorias = Button(painel_adm, text="Gerenciar categorias", width=25, command=panel_categorias)
    btnGerenciarCategorias.place(x=520, y=570)

    # botão gerenciar notificações
    btnNotificações = Button(painel_adm, text="Gerir notificações", width=25, command=panel_gerir_notificacoes)
    btnNotificações.place(x=520, y=525)
    # info user
    name= retrieve_current_user_data()
    username= retrieve_current_user_data()
    icon = retrieve_current_user_data()

    userInfoName = "Nome: " + str(name[0])
    label_userInfoName = Label(painel_adm, text=userInfoName, bg="#121212", fg="white")
    label_userInfoName.place (x=460, y=340)

    userInfoUsername = "Username: " + str(username[1])
    label_userInfoUsername = Label(painel_adm, text=userInfoUsername, bg="#121212", fg="white")
    label_userInfoUsername.place (x=460, y=370)

    admTxt = Label(painel_adm, text="Função: administrador", width=24, bd=0, bg="#121212", fg="white")
    admTxt.place(x=440, y=400)

    global imgBolinhas2
    imgBolinhas2 = PhotoImage(file= "./imgs/painel_login/notas_musicais_bolinhas.png")
    labelImg2 = Label(painel_adm, image=imgBolinhas2, width=300, height=600, bg="#121212")
    labelImg2.place(x=800, y=50)
    

    painel_adm.mainloop()

## - - - - - - - - - - CONTAINER SEARCH - - - - - - - - - - ##

def panel_search():
    global currentpanel
    currentpanel.pack_forget()

    panel_search = PanedWindow(window, width=1080, height=720)
    panel_search.place(x=0,y=0)
    currentpanel = panel_search
    panel_search.configure(bg="#121212")

    btnVoltar = Button(panel_search, text="Voltar", width=20, command=panel_account)
    btnVoltar.place(x=920, y=20)

    global lbCategorias
    lblCategorias = Label(panel_search, text = "Filtro por Categorias", bg="#121212", fg = "white", font=("Helvetica", 11))
    lblCategorias.place(x = 20, y = 10)
    lbCategorias = Listbox(panel_search, width=20, height=8, bg="#121212", fg = "white", selectbackground="#1db954")
    ListBoxCategorias(lbCategorias)
    lbCategorias.place(x = 20, y = 40)

    BtnNext = Button(panel_search, text = ">", command= lambda: [selecaoItem(lbCategorias), filtrarAlbums(treeCategorias, numAlbumCat)])
    BtnNext.place(x = 160, y = 100)

    def on_select(event):
        selected_item = treeCategorias.selection()[0]
        global select
        select = treeCategorias.item(selected_item)["values"][0]
        return select

    treeCategorias = ttk.Treeview(panel_search, height = 5, selectmode="browse", columns=("ID", "Álbum", "Artista", "Ano"), show = "headings")

    treeCategorias.column("ID", width=14, anchor="w")
    treeCategorias.column("Álbum", width=200, anchor="w")
    treeCategorias.column("Artista", width=150, anchor="w")
    treeCategorias.column("Ano", width=100, anchor="c")
    treeCategorias.heading("ID", text = "ID")
    treeCategorias.heading("Álbum", text = "Álbum")
    treeCategorias.heading("Artista", text = "Artista")
    treeCategorias.heading("Ano", text = "Ano")
    treeCategorias.place(x = 200, y = 40)
    treeCategorias.bind("<<TreeviewSelect>>", on_select)

    lbNumAlbumCat = Label(panel_search, text = "Nº de álbums", bg="#121212", fg = "white", font = ("Helvetica", "10"))
    lbNumAlbumCat.place(x=220, y=180)
    global numAlbumCat
    numAlbumCat = StringVar()
    txtNumAlbumCat = Entry(panel_search, width=10, textvariable = numAlbumCat, state="disable")
    txtNumAlbumCat.place(x=320, y=180)

    verscrlbar = ttk.Scrollbar(panel_search, orient="vertical", command= treeCategorias.yview)
    verscrlbar.place(x = 670+2, y=40+2, height=112+10)
    treeCategorias.configure(yscrollcommand=verscrlbar.set)

    btnPag = Button(panel_search, text = "Página do álbum", command = lambda: generate_page_album(select))
    btnPag.place(x = 450, y = 180)

    lblCategorias = Label(panel_search, text = "Filtro por Visualizações", bg="#121212", fg = "white", font=("Helvetica", 11))
    lblCategorias.place(x = 20, y = 220)

    def on_select1(event):
        selected_item2 = treeVisualicacao.selection()[0]
        global select1
        select1 = treeVisualicacao.item(selected_item2)["values"][0]
        print(select1)
        return select1

    treeVisualicacao = ttk.Treeview(panel_search, height = 5, selectmode="browse", columns=("ID", "Álbum", "Artista", "Visualizações"), show = "headings")

    treeVisualicacao.column("ID", width=14, anchor="w")
    treeVisualicacao.column("Álbum", width=200, anchor="c")
    treeVisualicacao.column("Artista", width=150, anchor="c")
    treeVisualicacao.column("Visualizações", width=100, anchor="c")
    treeVisualicacao.heading("ID", text = "ID")
    treeVisualicacao.heading("Álbum", text = "Álbum")
    treeVisualicacao.heading("Artista", text = "Artista")
    treeVisualicacao.heading("Visualizações", text = "Visualizações")
    treeVisualicacao.place(x = 20, y = 260)
    treeVisualicacao.bind("<<TreeviewSelect>>", on_select1)

    listaViews= lerViews()
    
    refreshTreeViews(listaViews, treeVisualicacao)

    lbNumAlbum = Label(panel_search, text = "Nº de álbums", bg="#121212", fg = "white", font = ("Helvetica", "10"))
    lbNumAlbum.place(x=20, y=400)
    txtNumAlbumVisu = Label(panel_search, width=10, text = "5", state="disable", anchor="w")
    txtNumAlbumVisu.place(x = 120, y=400)
    btnPagVis = Button(panel_search, text = "Página do álbum", command = lambda: generate_page_album(select1))
    btnPagVis.place(x = 250, y = 400)


    lblCategorias = Label(panel_search, text = "Filtro por Avaliações", bg="#121212", fg = "white", font=("Helvetica", 11))
    lblCategorias.place(x = 20, y = 450)

    def on_select2(event):
        selected_item3 = treeAvaliacao.selection()[0]
        global select2
        select2 = treeAvaliacao.item(selected_item3)["values"][0]
        print(select2)
        return select2

    treeAvaliacao = ttk.Treeview(panel_search, height = 5, selectmode="browse", columns=("ID", "Álbum", "Artista", "Avaliações"), show = "headings")

    treeAvaliacao.column("ID", width=14, anchor="w")
    treeAvaliacao.column("Álbum", width=200, anchor="c")
    treeAvaliacao.column("Artista", width=150, anchor="c")
    treeAvaliacao.column("Avaliações", width=100, anchor="c")
    treeAvaliacao.heading("ID", text = "ID")
    treeAvaliacao.heading("Álbum", text = "Álbum")
    treeAvaliacao.heading("Artista", text = "Artista")
    treeAvaliacao.heading("Avaliações", text = "Avaliações")
    treeAvaliacao.place(x = 20, y = 480)
    treeAvaliacao.bind("<<TreeviewSelect>>", on_select2)

    listaAvaliacao = lerScore()
    
    refreshTreeViews(listaAvaliacao, treeAvaliacao)

    lbNumAlbum = Label(panel_search, text = "Nº de álbums", bg="#121212", fg = "white", font = ("Helvetica", "10"))
    lbNumAlbum.place(x=20, y=400)
    txtNumAlbumScore = Label(panel_search, width=10, text = "5", state="disable", anchor="w")
    txtNumAlbumScore.place(x = 120, y=400)
    btnPagScore = Button(panel_search, text = "Página do álbum", command = lambda: generate_page_album(select2))
    btnPagScore.place(x = 250, y = 500)

    panel_search.mainloop()


## - - - - - - - - - - CONTAINER CATEGORIAS - - - - - - - - - - ##

def panel_categoriaPop():
    global currentpanel
    currentpanel.pack_forget()

    panel_categoriaPop = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_categoriaPop
    panel_categoriaPop.configure(bg="#121212")

    #coloca título da app
    lblTitulo = Label(panel_categoriaPop, text ="Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    global imgSearch
    imgSearch = PhotoImage(file ="./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (panel_categoriaPop, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    global imgUser
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (panel_categoriaPop, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    global imgNotific
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

    btnGuardarN = Button (panel_categoriaPop, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
    btnGuardarN.place (x = 930 , y = 9)
    btnGuardarN.bind('<Enter>', panel_notifications)

    # botao voltar
    btn_voltar = Button(panel_categoriaPop, text="Voltar", width=20, command=panel_homepage)
    btn_voltar.place(x=840, y=640)

    #coloca título da categoria
    lblTitulo = Label(panel_categoriaPop, text ="Destaques da categoria POP", bg="#121212", fg="white", font = "Arial, 15",relief = "flat")
    lblTitulo.place (x=100, y=150)

    #imagens
    global imgAlbum1
    global imgAlbum2
    global imgAlbum3
    global imgAlbum4
    global imgAlbum5
    global imgAlbum6

    imgAlbum1 = PhotoImage(file="imgs/covers/Hold_the_Girl.png", height= 150, width= 150)
    btnGuardarA1 = Button(panel_categoriaPop, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(1))
    btnGuardarA1.place (x = 100 , y = 212)
    tituloA1 = Label(panel_categoriaPop, text="Hold the Girl", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA1.place(x=92, y=377)

    imgAlbum2 = PhotoImage(file="imgs/covers/Harry's_House.png", height= 150, width= 150)
    btnGuardarA2 = Button (panel_categoriaPop, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(2))   
    btnGuardarA2.place (x = 350 , y = 212)
    tituloA2 = Label(panel_categoriaPop, text="Harry´s House", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA2.place(x=342, y=377)

    imgAlbum3 = PhotoImage(file="imgs/covers/Midnights.png", height= 150, width= 150)
    btnGuardarA3 = Button (panel_categoriaPop, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(3))   #174px album +nome
    btnGuardarA3.place (x = 600 , y = 212)   #180px distancia de um album pra outro
    tituloA3 = Label(panel_categoriaPop, text="Midnights", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA3.place(x=592, y=377)

    imgAlbum4 = PhotoImage(file="imgs/covers/Happier_Than_Ever.png", height= 150, width= 150)
    btnGuardarA4 = Button (panel_categoriaPop, width = 150, height = 150, image = imgAlbum4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(4))   #174px album +nome
    btnGuardarA4.place (x = 100 , y = 460)   #180px distancia de um album pra outro
    tituloA4 = Label(panel_categoriaPop, text="Happier Than Ever", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA4.place(x=92, y=625)

    imgAlbum5 = PhotoImage(file="imgs/covers/SOUR.png", height= 150, width= 150)
    btnGuardarA5 = Button (panel_categoriaPop, width = 150, height = 150, image = imgAlbum5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(5))   #174px album +nome
    btnGuardarA5.place (x = 350 , y = 460)   #180px distancia de um album pra outro
    tituloA5 = Label(panel_categoriaPop, text="SOUR", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA5.place(x=342, y=625)

    imgAlbum6 = PhotoImage(file="imgs/covers/Future_Nostalgia.png", height= 150, width= 150)
    btnGuardarA6 = Button (panel_categoriaPop, width = 150, height = 150, image = imgAlbum6, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(6))   #174px album +nome
    btnGuardarA6.place (x = 600 , y = 460)   #180px distancia de um album pra outro
    tituloA6 = Label(panel_categoriaPop, text="Future Nostalgia", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA6.place(x=592, y=625)

    panel_categoriaPop.place(x=0,y=0)


# ------------------------------------------------------
def panel_categoriaHiphop():
    global currentpanel
    currentpanel.pack_forget()

    panel_categoriaHiphop = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_categoriaHiphop
    panel_categoriaHiphop.configure(bg="#121212")

    #coloca título da app
    lblTitulo = Label(panel_categoriaHiphop, text ="Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    global imgSearch
    imgSearch = PhotoImage(file ="./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (panel_categoriaHiphop, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    global imgUser
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (panel_categoriaHiphop, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    global imgNotific
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

    btnGuardarN = Button (panel_categoriaHiphop, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
    btnGuardarN.place (x = 930 , y = 9)
    btnGuardarN.bind('<Enter>', panel_notifications)

    # botao voltar
    btn_voltar = Button(panel_categoriaHiphop, text="Voltar", width=20, command=panel_homepage)
    btn_voltar.place(x=840, y=640)

    #coloca título da categoria
    lblTitulo = Label(panel_categoriaHiphop, text ="Destaques da categoria HIP-POP", bg="#121212", fg="white", font = "Arial, 15",relief = "flat")
    lblTitulo.place (x=100, y=150)

    #imagens
    global imgAlbum1
    global imgAlbum2
    global imgAlbum3
    global imgAlbum4
    global imgAlbum5
    global imgAlbum6

    imgAlbum1 = PhotoImage(file="imgs/covers/This_Is_What_I_Mean.png", height= 150, width= 150)
    btnGuardarA1 = Button(panel_categoriaHiphop, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(7))
    btnGuardarA1.place (x = 100 , y = 212)
    tituloA1 = Label(panel_categoriaHiphop, text="This Is What I Mean", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA1.place(x=92, y=377)

    imgAlbum2 = PhotoImage(file="imgs/covers/23.png", height= 150, width= 150)
    btnGuardarA2 = Button (panel_categoriaHiphop, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(8))   
    btnGuardarA2.place (x = 350 , y = 212)
    tituloA2 = Label(panel_categoriaHiphop, text="23", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA2.place(x=342, y=377)

    imgAlbum3 = PhotoImage(file="imgs/covers/Honestly_Nevermind.png", height= 150, width= 150)
    btnGuardarA3 = Button (panel_categoriaHiphop, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(9))   #174px album +nome
    btnGuardarA3.place (x = 600 , y = 212)   #180px distancia de um album pra outro
    tituloA3 = Label(panel_categoriaHiphop, text="Honestly, Nevermind", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA3.place(x=592, y=377)

    imgAlbum4 = PhotoImage(file="imgs/covers/Come_Home_the_Kids_Miss_You.png", height= 150, width= 150)
    btnGuardarA4 = Button (panel_categoriaHiphop, width = 150, height = 150, image = imgAlbum4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(10))   #174px album +nome
    btnGuardarA4.place (x = 100 , y = 460)   #180px distancia de um album pra outro
    tituloA4 = Label(panel_categoriaHiphop, text="Come Home the Kids Miss You", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA4.place(x=92, y=625)

    imgAlbum5 = PhotoImage(file="imgs/covers/The_Divine_Feminine.png", height= 150, width= 150)
    btnGuardarA5 = Button (panel_categoriaHiphop, width = 150, height = 150, image = imgAlbum5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(11))   #174px album +nome
    btnGuardarA5.place (x = 350 , y = 460)   #180px distancia de um album pra outro
    tituloA5 = Label(panel_categoriaHiphop, text="The Divine Feminine", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA5.place(x=342, y=625)

    imgAlbum6 = PhotoImage(file="imgs/covers/777.png", height= 150, width= 150)
    btnGuardarA6 = Button (panel_categoriaHiphop, width = 150, height = 150, image = imgAlbum6, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(12))   #174px album +nome
    btnGuardarA6.place (x = 600 , y = 460)   #180px distancia de um album pra outro
    tituloA6 = Label(panel_categoriaHiphop, text="777", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA6.place(x=592, y=625)

    panel_categoriaHiphop.place(x=0,y=0)

# ------------------------------------------------------
def panel_categoriaKpop():
    global currentpanel
    currentpanel.pack_forget()

    panel_categoriaKpop = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_categoriaKpop
    panel_categoriaKpop.configure(bg="#121212")

    #coloca título da app
    lblTitulo = Label(panel_categoriaKpop, text ="Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    global imgSearch
    imgSearch = PhotoImage(file ="./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (panel_categoriaKpop, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    global imgUser
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (panel_categoriaKpop, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    global imgNotific
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

    btnGuardarN = Button (panel_categoriaKpop, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
    btnGuardarN.place (x = 930 , y = 9)
    btnGuardarN.bind('<Enter>', panel_notifications)

    # botao voltar
    btn_voltar = Button(panel_categoriaKpop, text="Voltar", width=20, command=panel_homepage)
    btn_voltar.place(x=840, y=640)

    #coloca título da categoria
    lblTitulo = Label(panel_categoriaKpop, text ="Destaques da categoria K-POP", bg="#121212", fg="white", font = "Arial, 15",relief = "flat")
    lblTitulo.place (x=100, y=150)

    #imagens
    global imgAlbum1
    global imgAlbum2
    global imgAlbum3
    global imgAlbum4
    global imgAlbum5
    global imgAlbum6

    imgAlbum1 = PhotoImage(file="imgs/covers/I_Never_Die.png", height= 150, width= 150)
    btnGuardarA1 = Button(panel_categoriaKpop, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(13))
    btnGuardarA1.place (x = 100 , y = 212)
    tituloA1 = Label(panel_categoriaKpop, text="I Never Die", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA1.place(x=92, y=377)

    imgAlbum2 = PhotoImage(file="imgs/covers/Between_1&2.png", height= 150, width= 150)
    btnGuardarA2 = Button (panel_categoriaKpop, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(14))   
    btnGuardarA2.place (x = 350 , y = 212)
    tituloA2 = Label(panel_categoriaKpop, text="Between 1&2", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA2.place(x=342, y=377)

    imgAlbum3 = PhotoImage(file="imgs/covers/Checkmate.png", height= 150, width= 150)
    btnGuardarA3 = Button (panel_categoriaKpop, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(15))   #174px album +nome
    btnGuardarA3.place (x = 600 , y = 212)   #180px distancia de um album pra outro
    tituloA3 = Label(panel_categoriaKpop, text="Checkmate", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA3.place(x=592, y=377)

    imgAlbum4 = PhotoImage(file="imgs/covers/Girls.png", height= 150, width= 150)
    btnGuardarA4 = Button (panel_categoriaKpop, width = 150, height = 150, image = imgAlbum4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(16))   #174px album +nome
    btnGuardarA4.place (x = 100 , y = 460)   #180px distancia de um album pra outro
    tituloA4 = Label(panel_categoriaKpop, text="Girls", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA4.place(x=92, y=625)

    imgAlbum5 = PhotoImage(file="imgs/covers/Born_Pink.png", height= 150, width= 150)
    btnGuardarA5 = Button (panel_categoriaKpop, width = 150, height = 150, image = imgAlbum5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(17))   #174px album +nome
    btnGuardarA5.place (x = 350 , y = 460)   #180px distancia de um album pra outro
    tituloA5 = Label(panel_categoriaKpop, text="Born Pink", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA5.place(x=342, y=625)

    imgAlbum6 = PhotoImage(file="imgs/covers/IM_NAYEON.png", height= 150, width= 150)
    btnGuardarA6 = Button (panel_categoriaKpop, width = 150, height = 150, image = imgAlbum6, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(18))   #174px album +nome
    btnGuardarA6.place (x = 600 , y = 460)   #180px distancia de um album pra outro
    tituloA6 = Label(panel_categoriaKpop, text="I'M NAYEON", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA6.place(x=592, y=625)

    panel_categoriaKpop.place(x=0,y=0)


    # ------------------------------------------------------
def panel_categoriaRock():
    global currentpanel
    currentpanel.pack_forget()

    panel_categoriaRock = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_categoriaRock
    panel_categoriaRock.configure(bg="#121212")

    #coloca título da app
    lblTitulo = Label(panel_categoriaRock, text ="Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    global imgSearch
    imgSearch = PhotoImage(file ="./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (panel_categoriaRock, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    global imgUser
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (panel_categoriaRock, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    global imgNotific
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

    btnGuardarN = Button (panel_categoriaRock, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
    btnGuardarN.place (x = 930 , y = 9)
    btnGuardarN.bind('<Enter>', panel_notifications)

    # botao voltar
    btn_voltar = Button(panel_categoriaRock, text="Voltar", width=20, command=panel_homepage)
    btn_voltar.place(x=840, y=640)

    #coloca título da categoria
    lblTitulo = Label(panel_categoriaRock, text ="Destaques da categoria ROCK", bg="#121212", fg="white", font = "Arial, 15",relief = "flat")
    lblTitulo.place (x=100, y=150)

    #imagens
    global imgAlbum1
    global imgAlbum2
    global imgAlbum3
    global imgAlbum4
    global imgAlbum5
    global imgAlbum6

    imgAlbum1 = PhotoImage(file="imgs/covers/The_Car.png", height= 150, width= 150)
    btnGuardarA1 = Button(panel_categoriaRock, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(19))
    btnGuardarA1.place (x = 100 , y = 212)
    tituloA1 = Label(panel_categoriaRock, text="The car", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA1.place(x=92, y=377)

    imgAlbum2 = PhotoImage(file="imgs/covers/Rumours.png", height= 150, width= 150)
    btnGuardarA2 = Button (panel_categoriaRock, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(20))   
    btnGuardarA2.place (x = 350 , y = 212)
    tituloA2 = Label(panel_categoriaRock, text="Rumours", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA2.place(x=342, y=377)

    imgAlbum3 = PhotoImage(file="imgs/covers/Nevermind.png", height= 150, width= 150)
    btnGuardarA3 = Button (panel_categoriaRock, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(21))   #174px album +nome
    btnGuardarA3.place (x = 600 , y = 212)   #180px distancia de um album pra outro
    tituloA3 = Label(panel_categoriaRock, text="Nevermind", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA3.place(x=592, y=377)

    imgAlbum4 = PhotoImage(file="imgs/covers/The_Dark_Side_of_the_Moon.png", height= 150, width= 150)
    btnGuardarA4 = Button (panel_categoriaRock, width = 150, height = 150, image = imgAlbum4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(22))   #174px album +nome
    btnGuardarA4.place (x = 100 , y = 460)   #180px distancia de um album pra outro
    tituloA4 = Label(panel_categoriaRock, text="The dark side of the moon", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA4.place(x=92, y=625)

    imgAlbum5 = PhotoImage(file="imgs/covers/Ok_Computer.png", height= 150, width= 150)
    btnGuardarA5 = Button (panel_categoriaRock, width = 150, height = 150, image = imgAlbum5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(23))   #174px album +nome
    btnGuardarA5.place (x = 350 , y = 460)   #180px distancia de um album pra outro
    tituloA5 = Label(panel_categoriaRock, text="OK Computer", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA5.place(x=342, y=625)

    imgAlbum6 = PhotoImage(file="imgs/covers/A_Night_at_the_Opera_Queen.png", height= 150, width= 150)
    btnGuardarA6 = Button (panel_categoriaRock, width = 150, height = 150, image = imgAlbum6, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(24))   #174px album +nome
    btnGuardarA6.place (x = 600 , y = 460)   #180px distancia de um album pra outro
    tituloA6 = Label(panel_categoriaRock, text="A night at the opera", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA6.place(x=592, y=625)

    panel_categoriaRock.place(x=0,y=0)


    # ------------------------------------------------------
def panel_categoriaReB():
    global currentpanel
    currentpanel.pack_forget()

    panel_categoriaReB = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_categoriaReB
    panel_categoriaReB.configure(bg="#121212")

    #coloca título da app
    lblTitulo = Label(panel_categoriaReB, text ="Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    global imgSearch
    imgSearch = PhotoImage(file ="./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (panel_categoriaReB, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    global imgUser
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (panel_categoriaReB, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    global imgNotific
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

    btnGuardarN = Button (panel_categoriaReB, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
    btnGuardarN.place (x = 930 , y = 9)
    btnGuardarN.bind('<Enter>', panel_notifications)

    # botao voltar
    btn_voltar = Button(panel_categoriaReB, text="Voltar", width=20, command=panel_homepage)
    btn_voltar.place(x=840, y=640)

    #coloca título da categoria
    lblTitulo = Label(panel_categoriaReB, text ="Destaques da categoria R&B", bg="#121212", fg="white", font = "Arial, 15",relief = "flat")
    lblTitulo.place (x=100, y=150)

    #imagens
    global imgAlbum1
    global imgAlbum2
    global imgAlbum3
    global imgAlbum4
    global imgAlbum5
    global imgAlbum6

    imgAlbum1 = PhotoImage(file="imgs/covers/An_Evening_with_Silk_Sonic.png", height= 150, width= 150)
    btnGuardarA1 = Button(panel_categoriaReB, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(25))
    btnGuardarA1.place (x = 100 , y = 212)
    tituloA1 = Label(panel_categoriaReB, text="An evening with Silk Sonic", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA1.place(x=92, y=377)

    imgAlbum2 = PhotoImage(file="imgs/covers/Thriller.png", height= 150, width= 150)
    btnGuardarA2 = Button (panel_categoriaReB, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(26))   
    btnGuardarA2.place (x = 350 , y = 212)
    tituloA2 = Label(panel_categoriaReB, text="Thriller", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA2.place(x=342, y=377)

    imgAlbum3 = PhotoImage(file="imgs/covers/Gemini_Rights.png", height= 150, width= 150)
    btnGuardarA3 = Button (panel_categoriaReB, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(27))   #174px album +nome
    btnGuardarA3.place (x = 600 , y = 212)   #180px distancia de um album pra outro
    tituloA3 = Label(panel_categoriaReB, text="Gemini Rights", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA3.place(x=592, y=377)

    imgAlbum4 = PhotoImage(file="imgs/covers/Whats_Going_On.png", height= 150, width= 150)
    btnGuardarA4 = Button (panel_categoriaReB, width = 150, height = 150, image = imgAlbum4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(28))   #174px album +nome
    btnGuardarA4.place (x = 100 , y = 460)   #180px distancia de um album pra outro
    tituloA4 = Label(panel_categoriaReB, text="What's Going On", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA4.place(x=92, y=625)

    imgAlbum5 = PhotoImage(file="imgs/covers/innervisions.png", height= 150, width= 150)
    btnGuardarA5 = Button (panel_categoriaReB, width = 150, height = 150, image = imgAlbum5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(29))   #174px album +nome
    btnGuardarA5.place (x = 350 , y = 460)   #180px distancia de um album pra outro
    tituloA5 = Label(panel_categoriaReB, text="Innervisions", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA5.place(x=342, y=625)

    imgAlbum6 = PhotoImage(file="imgs/covers/No_Thank_You.png", height= 150, width= 150)
    btnGuardarA6 = Button (panel_categoriaReB, width = 150, height = 150, image = imgAlbum6, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(30))   #174px album +nome
    btnGuardarA6.place (x = 600 , y = 460)   #180px distancia de um album pra outro
    tituloA6 = Label(panel_categoriaReB, text="No Thank You", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA6.place(x=592, y=625)

    panel_categoriaReB.place(x=0,y=0)


    # ------------------------------------------------------
def panel_categoriaCountry():
    global currentpanel
    currentpanel.pack_forget()

    panel_categoriaCountry = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_categoriaCountry
    panel_categoriaCountry.configure(bg="#121212")

    #coloca título da app
    lblTitulo = Label(panel_categoriaCountry, text ="Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    global imgSearch
    imgSearch = PhotoImage(file ="./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (panel_categoriaCountry, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    global imgUser
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (panel_categoriaCountry, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    global imgNotific
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

    btnGuardarN = Button (panel_categoriaCountry, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
    btnGuardarN.place (x = 930 , y = 9)
    btnGuardarN.bind('<Enter>', panel_notifications)

    # botao voltar
    btn_voltar = Button(panel_categoriaCountry, text="Voltar", width=20, command=panel_homepage)
    btn_voltar.place(x=840, y=640)

    #coloca título da categoria
    lblTitulo = Label(panel_categoriaCountry, text ="Destaques da categoria Country", bg="#121212", fg="white", font = "Arial, 15",relief = "flat")
    lblTitulo.place (x=100, y=150)

    #imagens
    global imgAlbum1
    global imgAlbum2
    global imgAlbum3
    global imgAlbum4
    global imgAlbum5
    global imgAlbum6

    imgAlbum1 = PhotoImage(file="imgs/covers/I_Know_Im_Funny_Haha.png", height= 150, width= 150)
    btnGuardarA1 = Button(panel_categoriaCountry, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(31))
    btnGuardarA1.place (x = 100 , y = 212)
    tituloA1 = Label(panel_categoriaCountry, text="I Know I'm Funny Haha", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA1.place(x=92, y=377)

    imgAlbum2 = PhotoImage(file="imgs/covers/Show_Pony.png", height= 150, width= 150)
    btnGuardarA2 = Button (panel_categoriaCountry, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(32))   
    btnGuardarA2.place (x = 350 , y = 212)
    tituloA2 = Label(panel_categoriaCountry, text="Show Pony", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA2.place(x=342, y=377)

    imgAlbum3 = PhotoImage(file="imgs/covers/Laura_Stevenson.png", height= 150, width= 150)
    btnGuardarA3 = Button (panel_categoriaCountry, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(33))   #174px album +nome
    btnGuardarA3.place (x = 600 , y = 212)   #180px distancia de um album pra outro
    tituloA3 = Label(panel_categoriaCountry, text="Laura Stevenson", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA3.place(x=592, y=377)

    imgAlbum4 = PhotoImage(file="imgs/covers/The_Hardest_Part.png", height= 150, width= 150)
    btnGuardarA4 = Button (panel_categoriaCountry, width = 150, height = 150, image = imgAlbum4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(34))   #174px album +nome
    btnGuardarA4.place (x = 100 , y = 460)   #180px distancia de um album pra outro
    tituloA4 = Label(panel_categoriaCountry, text="The Hardest Part", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA4.place(x=92, y=625)

    imgAlbum5 = PhotoImage(file="imgs/covers/Saint_Cloud.png", height= 150, width= 150)
    btnGuardarA5 = Button (panel_categoriaCountry, width = 150, height = 150, image = imgAlbum5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(35))   #174px album +nome
    btnGuardarA5.place (x = 350 , y = 460)   #180px distancia de um album pra outro
    tituloA5 = Label(panel_categoriaCountry, text="Saint Cloud", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA5.place(x=342, y=625)

    imgAlbum6 = PhotoImage(file="imgs/covers/Why_Not_Me.png", height= 150, width= 150)
    btnGuardarA6 = Button (panel_categoriaCountry, width = 150, height = 150, image = imgAlbum6, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(36))   #174px album +nome
    btnGuardarA6.place (x = 600 , y = 460)   #180px distancia de um album pra outro
    tituloA6 = Label(panel_categoriaCountry, text="Why Not Me", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA6.place(x=592, y=625)

    panel_categoriaCountry.place(x=0,y=0)


        # ------------------------------------------------------
def panel_categoriaOutros():
    global currentpanel
    currentpanel.pack_forget()

    panel_categoriaOutros = PanedWindow(window, width=1080, height=720)
    currentpanel = panel_categoriaOutros
    panel_categoriaOutros.configure(bg="#121212")

    #coloca título da app
    lblTitulo = Label(panel_categoriaOutros, text ="Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    global imgSearch
    imgSearch = PhotoImage(file ="./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (panel_categoriaOutros, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    global imgUser
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (panel_categoriaOutros, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    global imgNotific
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

    btnGuardarN = Button (panel_categoriaOutros, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
    btnGuardarN.place (x = 930 , y = 9)
    btnGuardarN.bind('<Enter>', panel_notifications)

    # botao voltar
    btn_voltar = Button(panel_categoriaOutros, text="Voltar", width=20, command=panel_homepage)
    btn_voltar.place(x=840, y=640)

    #coloca título da categoria
    lblTitulo = Label(panel_categoriaOutros, text ="Destaques da categoria R&B", bg="#121212", fg="white", font = "Arial, 15",relief = "flat")
    lblTitulo.place (x=100, y=150)

    #imagens
    global imgAlbum1
    global imgAlbum2
    global imgAlbum3


    imgAlbum1 = PhotoImage(file="imgs/covers/Raising_Cain.png", height= 150, width= 150)
    btnGuardarA1 = Button(panel_categoriaOutros, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(37))
    btnGuardarA1.place (x = 100 , y = 212)
    tituloA1 = Label(panel_categoriaOutros, text="Hell on Earth", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA1.place(x=92, y=377)

    imgAlbum2 = PhotoImage(file="imgs/covers/Hear_Me_Now.png", height= 150, width= 150)
    btnGuardarA2 = Button (panel_categoriaOutros, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(38))   
    btnGuardarA2.place (x = 350 , y = 212)
    tituloA2 = Label(panel_categoriaOutros, text="Hear me now", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA2.place(x=342, y=377)

    imgAlbum3 = PhotoImage(file="imgs/covers/Cantor_De_Sonhos.png", height= 150, width= 150)
    btnGuardarA3 = Button (panel_categoriaOutros, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(39))   #174px album +nome
    btnGuardarA3.place (x = 600 , y = 212)   #180px distancia de um album pra outro
    tituloA3 = Label(panel_categoriaOutros, text="Cantor de Sonhos", width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA3.place(x=592, y=377)


    panel_categoriaOutros.place(x=0,y=0)

## - - - - - - - - - - CONTAINER HOMEPAGE - - - - - - - - - - ##

def panel_homepage():
    global currentpanel
    currentpanel.pack_forget()

    home_pageP = PanedWindow(window, width=1080, height=720)
    home_pageP.place(x=0,y=0)
    currentpanel = home_pageP
    home_pageP.configure(bg="#121212")

    window.title('   Songsy')
    window.resizable(0,0)
    window.iconbitmap("./imgs/home/music.ico")

    #coloca título da app
    lblTitulo = Label(home_pageP, text = "Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
    lblTitulo.place (x=500, y=5)

    #define icone da lupa no botao de busca
    global imgSearch
    imgSearch = PhotoImage(file = "./imgs/home/search.png", height=20, width=20)
    btnGuardarS = Button (home_pageP, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
    btnGuardarS.place (x = 1020 , y = 7)

    #define icone de user no botao para ir p/ página do usuário
    global imgUser
    imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
    btnGuardarU = Button (home_pageP, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
    btnGuardarU.place (x = 975 , y = 9)

    #define icone de sino para ir pra página de notificações
    global imgNotific
    imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

    btnGuardarN = Button (home_pageP, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
    btnGuardarN.place (x = 930 , y = 9)
    btnGuardarN.bind('<Enter>', panel_notifications)

    # mostra os generos musicias suportados pela app
    btnPop = Button(home_pageP, text="POP", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaPop)
    btnPop.place(x=70, y=90)

    btnHiphop = Button(home_pageP, text="HIP-HOP", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaHiphop)
    btnHiphop.place(x=200, y=90)

    btnKpop = Button(home_pageP, text="K-POP", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaKpop)
    btnKpop.place(x=330, y=90)

    btnRock = Button(home_pageP, text="ROCK", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaRock)
    btnRock.place(x=460, y=90)

    btnReb = Button(home_pageP, text="R&B", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaReB)
    btnReb.place(x=590, y=90)

    btnCountry = Button(home_pageP, text="COUNTRY", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaCountry)
    btnCountry.place(x=720, y=90)

    btnOutros = Button(home_pageP, text="OUTROS", width=15, height=2,bg="white", fg="#121212", command=panel_categoriaOutros)
    btnOutros.place(x=850, y=90)


    #define Álbuns mais vistos cada botao levando a pagina do album
    maisOuvidosTxt = LabelFrame(home_pageP, text = "Álbuns mais visitados do momento", borderwidth=0, width= 1000, height=250, bg="#121212", fg="white", font="Arial, 10", relief="flat")
    maisOuvidosTxt.place (x=70, y=177)

    listaMaisVistos = idsMaisVistos()
    imagemMaisVisto1, nomeAlbMaisVisto1, artistaAlb1, infoAlb1, scoreAlb1, descpAlb1, idAlb1 = album_contents(listaMaisVistos[0])
    imagemMaisVisto2, nomeAlbMaisVisto2, artistaAlb2, infoAlb2, scoreAlb2, descpAlb2, idAlb2 = album_contents(listaMaisVistos[1])
    imagemMaisVisto3, nomeAlbMaisVisto3, artistaAlb3, infoAlb3, scoreAlb3, descpAlb3, idAlb3 = album_contents(listaMaisVistos[2])
    imagemMaisVisto4, nomeAlbMaisVisto4, artistaAlb4, infoAlb4, scoreAlb4, descpAlb4, idAlb4 = album_contents(listaMaisVistos[3])
    imagemMaisVisto5, nomeAlbMaisVisto5, artistaAlb5, infoAlb5, scoreAlb5, descpAlb5, idAlb5 = album_contents(listaMaisVistos[4])

    global imgAlbum1
    imgAlbum1 = PhotoImage(file = imagemMaisVisto1, height= 150, width= 150)
    btnGuardarA1 = Button(home_pageP, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[0]))
    btnGuardarA1.place (x = 70 , y = 212)
    tituloA1 = Label(home_pageP, text=nomeAlbMaisVisto1, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA1.place(x=62, y=377)

    global imgAlbum2
    imgAlbum2 = PhotoImage(file = imagemMaisVisto2, height= 150, width= 150)
    btnGuardarA2 = Button (home_pageP, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[1]))   
    btnGuardarA2.place (x = 250 , y = 212)
    tituloA2 = Label(home_pageP, text=nomeAlbMaisVisto2, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA2.place(x=242, y=377)

    global imgAlbum3
    imgAlbum3 = PhotoImage(file = imagemMaisVisto3, height= 150, width= 150)
    btnGuardarA3 = Button (home_pageP, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[2]))   #174px album +nome
    btnGuardarA3.place (x = 430 , y = 212)   #180px distancia de um album pra outro
    tituloA3 = Label(home_pageP, text= nomeAlbMaisVisto3, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA3.place(x=422, y=377)

    global imgAlbum4
    imgAlbum4 = PhotoImage(file = imagemMaisVisto4, height= 150, width= 150)
    btnGuardarA4 = Button (home_pageP, width = 150, height = 150, image = imgAlbum4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[3]))   #174px album +nome
    btnGuardarA4.place (x = 610 , y = 212)   #180px distancia de um album pra outro
    tituloA4 = Label(home_pageP, text= nomeAlbMaisVisto4, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA4.place(x=602, y=377)

    global imgAlbum5
    imgAlbum5 = PhotoImage(file = imagemMaisVisto5, height= 150, width= 150)
    btnGuardarA5 = Button (home_pageP, width = 150, height = 150, image = imgAlbum5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[4]))   #174px album +nome
    btnGuardarA5.place (x = 790 , y = 212)   #180px distancia de um album pra outro
    tituloA5 = Label(home_pageP, text= nomeAlbMaisVisto5, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloA5.place(x=784, y=377)


    listaMaisBemAvaliados = idsMaisAvaliados()
    imgavaliado1, album_nameavaliado1, album_artistavaliado1, album_infoavaliado1, album_scoreavaliado1, album_descriptionavaliado1, alb_idavaliado1 = album_contents(listaMaisBemAvaliados[0])
    imgavaliado2, album_nameavaliado2, album_artistavaliado2, album_infoavaliado2, album_scoreavaliado2, album_descriptionavaliado2, alb_idavaliado2 = album_contents(listaMaisBemAvaliados[1])
    imgavaliado3, album_nameavaliado3, album_artistavaliado3, album_infoavaliado3, album_scoreavaliado3, album_descriptionavaliado3, alb_idavaliado3 = album_contents(listaMaisBemAvaliados[2])
    imgavaliado4, album_nameavaliado4, album_artistavaliado4, album_infoavaliado4, album_scoreavaliado4, album_descriptionavaliado4, alb_idavaliado4 = album_contents(listaMaisBemAvaliados[3])
    imgavaliado5, album_nameavaliado5, album_artistavaliado5, album_infoavaliado5, album_scoreavaliado5, album_descriptionavaliado5, alb_idavaliado5 = album_contents(listaMaisBemAvaliados[4])

    favoritosTxt = LabelFrame(home_page, text = "TOP 5 mais bem avaliados", borderwidth=0, width= 1000, height=250, bg="#121212", fg="white", font="Arial, 10", relief="flat")
    favoritosTxt.place (x=70, y=463)

    global imgFav1
    imgFav1 = PhotoImage(file = imgavaliado1, height= 150, width= 150)
    btnGuardarF1 = Button (home_pageP, width = 150, height = 150, image = imgFav1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado1))
    btnGuardarF1.place (x = 70 , y = 498)
    tituloF1 = Label(home_pageP, text= album_nameavaliado1, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloF1.place(x=64, y=663)

    global imgFav2
    imgFav2 = PhotoImage(file = imgavaliado2, height= 150, width= 150)
    btnGuardarF2 = Button (home_pageP, width = 150, height = 150, image = imgFav2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado2))   
    btnGuardarF2.place (x = 250 , y = 498)
    tituloF2 = Label(home_pageP, text= album_nameavaliado2, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloF2.place(x=244, y=663)

    global imgFav3
    imgFav3 = PhotoImage(file = imgavaliado3, height= 150, width= 150)
    btnGuardarF3 = Button (home_pageP, width = 150, height = 150, image = imgFav3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado3))   #174px album +nome
    btnGuardarF3.place (x = 430 , y = 498)   
    tituloF3 = Label(home_pageP, text= album_nameavaliado3, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloF3.place(x=424, y=663)

    global imgFav4
    imgFav4 = PhotoImage(file = imgavaliado4, height= 150, width= 150)
    btnGuardarF4 = Button (home_pageP, width = 150, height = 150, image = imgFav4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado4))   #174px album +nome
    btnGuardarF4.place (x = 610 , y = 498)  
    tituloF4 = Label(home_pageP, text= album_nameavaliado4, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloF4.place(x=606, y=663)

    global imgFav5
    imgFav5 = PhotoImage(file = imgavaliado5, height= 150, width= 150)
    btnGuardarF5 = Button (home_pageP, width = 150, height = 150, image = imgFav5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado5))   #174px album +nome
    btnGuardarF5.place (x = 790 , y = 498)  
    tituloF5 = Label(home_pageP, text= album_nameavaliado5, width=24, height=3, bd=0, bg="#121212", fg="white")
    tituloF5.place(x=784, y=663)

    currentpanel = home_pageP

    home_page.place(x=0,y=0)



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
home_page.configure(bg = "#121212")

logout_user()

#coloca título da app
lblTitulo = Label(home_page, text = "Songsy", bg="#121212", fg="white", font = "Arial, 25",relief = "flat")
lblTitulo.place (x=500, y=5)

#define icone da lupa no botao de busca
global imgSearch
imgSearch = PhotoImage(file = "./imgs/home/search.png", height=20, width=20)
btnGuardarS = Button (home_page, width = 40, height = 40, image = imgSearch, border=0, bg="#121212", fg="white", command=panel_search)
btnGuardarS.place (x = 1020 , y = 7)

#define icone de user no botao para ir p/ página do usuário
global imgUser
imgUser = PhotoImage(file = "./imgs/home/user.png", height=20, width=20)
btnGuardarU = Button (home_page, width = 40, height = 40, image = imgUser, border=0, bg="#121212", fg="white", command=panel_login)
btnGuardarU.place (x = 975 , y = 9)

#define icone de sino para ir pra página de notificações
global imgNotific
imgNotific = PhotoImage(file = "./imgs/home/sino.png", height=20, width=20)

btnGuardarN = Button (home_page, width = 40, height = 40, image = imgNotific, border=0, bg="#121212", fg="white", command=panel_notifications)
btnGuardarN.place (x = 930 , y = 9)
btnGuardarN.bind('<Enter>', panel_notifications)

# mostra os generos musicias suportados pela app
btnPop = Button(home_page, text="POP", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaPop)
btnPop.place(x=70, y=90)

btnHiphop = Button(home_page, text="HIP-HOP", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaHiphop)
btnHiphop.place(x=200, y=90)

btnKpop = Button(home_page, text="K-POP", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaKpop)
btnKpop.place(x=330, y=90)

btnRock = Button(home_page, text="ROCK", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaRock)
btnRock.place(x=460, y=90)

btnReb = Button(home_page, text="R&B", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaReB)
btnReb.place(x=590, y=90)

btnCountry = Button(home_page, text="COUNTRY", width=15, height=2, bg="white", fg="#121212", command=panel_categoriaCountry)
btnCountry.place(x=720, y=90)

btnOutros = Button(home_page, text="OUTROS", width=15, height=2,bg="white", fg="#121212", command=panel_categoriaOutros)
btnOutros.place(x=850, y=90)


#define Álbuns mais vistos cada botao levando a pagina do album
maisOuvidosTxt = LabelFrame(home_page, text = "Álbuns mais visitados do momento", borderwidth=0, width= 1000, height=250, bg="#121212", fg="white", font="Arial, 10", relief="flat")
maisOuvidosTxt.place (x=70, y=177)

listaMaisVistos = idsMaisVistos()
imagemMaisVisto1, nomeAlbMaisVisto1, artistaAlb1, infoAlb1, scoreAlb1, descpAlb1, idAlb1 = album_contents(listaMaisVistos[0])
imagemMaisVisto2, nomeAlbMaisVisto2, artistaAlb2, infoAlb2, scoreAlb2, descpAlb2, idAlb2 = album_contents(listaMaisVistos[1])
imagemMaisVisto3, nomeAlbMaisVisto3, artistaAlb3, infoAlb3, scoreAlb3, descpAlb3, idAlb3 = album_contents(listaMaisVistos[2])
imagemMaisVisto4, nomeAlbMaisVisto4, artistaAlb4, infoAlb4, scoreAlb4, descpAlb4, idAlb4 = album_contents(listaMaisVistos[3])
imagemMaisVisto5, nomeAlbMaisVisto5, artistaAlb5, infoAlb5, scoreAlb5, descpAlb5, idAlb5 = album_contents(listaMaisVistos[4])

imgAlbum1 = PhotoImage(file = imagemMaisVisto1, height= 150, width= 150)
btnGuardarA1 = Button(home_page, width = 150, height = 150, image = imgAlbum1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[0]))
btnGuardarA1.place (x = 70 , y = 212)
tituloA1 = Label(home_page, text=nomeAlbMaisVisto1, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloA1.place(x=62, y=377)

imgAlbum2 = PhotoImage(file = imagemMaisVisto2, height= 150, width= 150)
btnGuardarA2 = Button (home_page, width = 150, height = 150, image = imgAlbum2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[1]))   
btnGuardarA2.place (x = 250 , y = 212)
tituloA2 = Label(home_page, text=nomeAlbMaisVisto2, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloA2.place(x=242, y=377)

imgAlbum3 = PhotoImage(file = imagemMaisVisto3, height= 150, width= 150)
btnGuardarA3 = Button (home_page, width = 150, height = 150, image = imgAlbum3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[2]))   #174px album +nome
btnGuardarA3.place (x = 430 , y = 212)   #180px distancia de um album pra outro
tituloA3 = Label(home_page, text= nomeAlbMaisVisto3, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloA3.place(x=422, y=377)

imgAlbum4 = PhotoImage(file = imagemMaisVisto4, height= 150, width= 150)
btnGuardarA4 = Button (home_page, width = 150, height = 150, image = imgAlbum4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[3]))   #174px album +nome
btnGuardarA4.place (x = 610 , y = 212)   #180px distancia de um album pra outro
tituloA4 = Label(home_page, text= nomeAlbMaisVisto4, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloA4.place(x=602, y=377)

imgAlbum5 = PhotoImage(file = imagemMaisVisto5, height= 150, width= 150)
btnGuardarA5 = Button (home_page, width = 150, height = 150, image = imgAlbum5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(listaMaisVistos[4]))   #174px album +nome
btnGuardarA5.place (x = 790 , y = 212)   #180px distancia de um album pra outro
tituloA5 = Label(home_page, text= nomeAlbMaisVisto5, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloA5.place(x=784, y=377)


#define Álbuns mais favoritados da app

listaMaisBemAvaliados = idsMaisAvaliados()
imgavaliado1, album_nameavaliado1, album_artistavaliado1, album_infoavaliado1, album_scoreavaliado1, album_descriptionavaliado1, alb_idavaliado1 = album_contents(listaMaisBemAvaliados[0])
imgavaliado2, album_nameavaliado2, album_artistavaliado2, album_infoavaliado2, album_scoreavaliado2, album_descriptionavaliado2, alb_idavaliado2 = album_contents(listaMaisBemAvaliados[1])
imgavaliado3, album_nameavaliado3, album_artistavaliado3, album_infoavaliado3, album_scoreavaliado3, album_descriptionavaliado3, alb_idavaliado3 = album_contents(listaMaisBemAvaliados[2])
imgavaliado4, album_nameavaliado4, album_artistavaliado4, album_infoavaliado4, album_scoreavaliado4, album_descriptionavaliado4, alb_idavaliado4 = album_contents(listaMaisBemAvaliados[3])
imgavaliado5, album_nameavaliado5, album_artistavaliado5, album_infoavaliado5, album_scoreavaliado5, album_descriptionavaliado5, alb_idavaliado5 = album_contents(listaMaisBemAvaliados[4])

favoritosTxt = LabelFrame(home_page, text = "TOP 5 mais bem avaliados", borderwidth=0, width= 1000, height=250, bg="#121212", fg="white", font="Arial, 10", relief="flat")
favoritosTxt.place (x=70, y=463)


imgFav1 = PhotoImage(file = imgavaliado1, height= 150, width= 150)
btnGuardarF1 = Button (home_page, width = 150, height = 150, image = imgFav1, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado1))
btnGuardarF1.place (x = 70 , y = 498)
tituloF1 = Label(home_page, text= album_nameavaliado1, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloF1.place(x=64, y=663)

imgFav2 = PhotoImage(file = imgavaliado2, height= 150, width= 150)
btnGuardarF2 = Button (home_page, width = 150, height = 150, image = imgFav2, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado2))   
btnGuardarF2.place (x = 250 , y = 498)
tituloF2 = Label(home_page, text= album_nameavaliado2, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloF2.place(x=244, y=663)

imgFav3 = PhotoImage(file = imgavaliado3, height= 150, width= 150)
btnGuardarF3 = Button (home_page, width = 150, height = 150, image = imgFav3, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado3))   #174px album +nome
btnGuardarF3.place (x = 430 , y = 498)   
tituloF3 = Label(home_page, text= album_nameavaliado3, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloF3.place(x=424, y=663)

imgFav4 = PhotoImage(file = imgavaliado4, height= 150, width= 150)
btnGuardarF4 = Button (home_page, width = 150, height = 150, image = imgFav4, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado4))   #174px album +nome
btnGuardarF4.place (x = 610 , y = 498)  
tituloF4 = Label(home_page, text= album_nameavaliado4, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloF4.place(x=606, y=663)

imgFav5 = PhotoImage(file = imgavaliado5, height= 150, width= 150)
btnGuardarF5 = Button (home_page, width = 150, height = 150, image = imgFav5, border=0, bg="#121212", fg="white", command=lambda:generate_page_album(alb_idavaliado5))   #174px album +nome
btnGuardarF5.place (x = 790 , y = 498)  

tituloF5 = Label(home_page, text= album_nameavaliado5, width=24, height=3, bd=0, bg="#121212", fg="white")
tituloF5.place(x=784, y=663)

currentpanel = home_page

window.mainloop()
