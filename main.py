from tkinter import *
import os
from users import *

## GUI implementation

#### PAGE SWITCHERS 

def logout_and_change_page(page):
    logout_user()
    page()

def login_and_change_page(username, password, page):
    if submit_login(username, password) == True:
        page()

## - - - - - - - - - - CONTAINER REGISTER - - - - - - - - - - ##

def panel_admin():
    global currentpanel
    currentpanel.pack_forget()

    window_admin = PanedWindow(window, width=1080, height=720)
    currentpanel = window_admin

    label_admin = Label(window_admin, text="Bem-vindo, administrador!", width=34)
    label_admin.place(x=400, y=200)

    window_admin.place(x=0, y=0)

def panel_edit_profile():
    global currentpanel
    currentpanel.pack_forget()

    window_edit_profile = PanedWindow(window, width=1080, height=720)
    currentpanel = window_edit_profile

    name, username, icon, bio = retrieve_current_user_data()

    name_text = "Teu nome atual é: " + name
    label_name = Label(window_edit_profile, text=name_text)
    label_name.place(x=20, y=50)

    username_text = "Teu username atual é: " + username
    label_username = Label(window_edit_profile, text=username_text)
    label_username.place(x=400, y=50)

    bio_text = "Tua bio atual é: "
    label_bio_text = Label(window_edit_profile, text=bio_text)
    label_bio = Label(window_edit_profile, justify='center', wraplength=240, text=bio)
    label_bio_text.place(x=20, y=220)
    label_bio.place(x=20, y=240)

    icon_text = "O teu icon atual é: "
    label_icon_text = Label(window_edit_profile, text=icon_text)
    label_icon_text.place(x=740, y=220)
    ficheiro_img = os.path.join('imgs\\profile_pics', icon)
    user_img = Canvas(window_edit_profile, width=100, height=100, bd=0)
    user_img.place(x=740, y=240)
    global img
    img = PhotoImage(file = ficheiro_img)
    user_img.create_image(50,50, anchor=CENTER, image = img)

    label_new_name = Label(window_edit_profile, text="Insira o teu novo nome:")
    label_new_name.place(x=20, y=80)
    new_name = name
    entry_new_name = Entry(window_edit_profile, width=30, textvariable=new_name)
    entry_new_name.place(x=20, y=100)

    label_new_username = Label(window_edit_profile, text="Insira o teu novo username:")
    label_new_username.place(x=400, y=80)
    new_username = username
    entry_new_username = Entry(window_edit_profile, width=30, textvariable=new_username)
    entry_new_username.place(x=400, y=100)

    label_new_bio = Label(window_edit_profile, text="Insira a tua nova bio:")
    label_new_bio.place(x=20, y=290)
    new_bio = bio
    entry_new_bio = Text(window_edit_profile) # usar GET para inserir conteúdo do Text em new_bio
    entry_new_bio.place(x=20, y=310, width=300, height=100)

    window_edit_profile.place(x=0, y=0)

def panel_register():
    global currentpanel
    currentpanel.pack_forget()

    window_register = PanedWindow(window, width=1080, height=720)
    window_register.place(x=0, y=0)
    currentpanel = window_register

    ficheiro_img = os.path.join('imgs\profile_pics', 'avatarnone.png')

    register_img = Canvas(window_register, width=100, height=100, bd=0)
    register_img.place(x=510, y=60)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    name_register = StringVar()
    label_name = Label(window_register, text="Nome completo:")
    entry_name = Entry(window_register, width=40, textvariable=name_register)
    label_name.place(x=440, y=220)
    entry_name.place(x=440, y=245)

    email_register = StringVar()
    label_email = Label(window_register, text="E-mail:")
    entry_email = Entry(window_register, width=40, textvariable=email_register)
    label_email.place(x=440, y=290)
    entry_email.place(x=440, y=315)

    username_register = StringVar()
    label_username = Label(window_register, text="Nome de usuário:")
    entry_username = Entry(window_register, width=40, textvariable=username_register)
    label_username.place(x=440, y=360)
    entry_username.place(x=440, y=385)

    password_register = StringVar()
    label_password = Label(window_register, text="Password:")
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

    ficheiro_img = os.path.join('imgs\profile_pics', 'avatarnone.png')

    register_img = Canvas(window_login, width=100, height=100, bd=0)
    register_img.place(x=510, y=60)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    username_login = StringVar()
    label_username = Label(window_login, text="Nome de usuário:")
    entry_username = Entry(window_login, width=40, textvariable=username_login)
    label_username.place(x=440, y=220)
    entry_username.place(x=440, y=245)

    password_login = StringVar()
    label_password = Label(window_login, text="Password:")
    entry_password = Entry(window_login, width=40, textvariable=password_login, show='*')
    label_password.place(x=440, y=290)
    entry_password.place(x=440, y=315)

    btn_submit_login = Button(window_login, text="Login", width=34, command= lambda: login_and_change_page(username_login.get(), password_login.get(), panel_account))
    btn_submit_login.place(x=440, y=380)

    btn_voltar = Button(window_login, text="Voltar", width=34, command=panel_homepage)
    btn_voltar.place(x=440, y=455)

    window_login.place(x=0, y=0)

## - - - - - - - - - - CONTAINER ACCOUNT - - - - - - - - - - ##

def panel_account():
    global currentpanel
    currentpanel.pack_forget()

    window_account = PanedWindow(window, width=1080, height=720)
    currentpanel = window_account

    name, username, icon, bio = retrieve_current_user_data()

    ficheiro_img = os.path.join('imgs\\profile_pics', icon)

    register_img = Canvas(window_account, width=100, height=100, bd=0)
    register_img.place(x=100, y=40)
    global img
    img = PhotoImage(file = ficheiro_img)
    register_img.create_image(50,50, anchor=CENTER, image = img)

    label_username = Label(window_account, text=name, font=("Helvetica", 24))
    label_username.place(x=220, y=40)

    text_label_username = '@' + username
    label_username = Label(window_account, text=text_label_username, font=("Helvetica", 12))
    label_username.place(x=220, y=90)

    label_username = Label(window_account, text=bio, justify='center', wraplength=240)
    label_username.place(x=100, y=160)

    btn_edit_profile = Button(window_account, text="Editar perfil", width=20, command=panel_edit_profile)
    btn_edit_profile.place(x=800, y=40)

    btn_logout = Button(window_account, text="Fazer logout", width=20, command= lambda: logout_and_change_page(panel_homepage))

    if username == 'admin':
        btn_admin = Button(window_account, text="Painel do administrador", width=20, command=panel_admin)
        btn_admin.place(x=800, y=90)
        btn_logout.place(x=800, y=140)
    else:
        btn_logout.place(x=800, y=90)

    window_account.place(x=0, y=0)

## - - - - - - - - - - CONTAINER HOMEPAGE - - - - - - - - - - ##

def panel_homepage():
    global currentpanel
    currentpanel.pack_forget()

    window_main = PanedWindow(window, width=1080, height=720)
    window_main.place(x=0,y=0)
    currentpanel = window_main

    btn_registrar = Button(window_main, text="Registar", command=panel_register)
    btn_registrar.place(x=500, y=360)

    btn_login = Button(window_main, text="Login", command=panel_login)
    btn_login.place(x=500, y=400)

## - - - - - - - - - - - - - - - - - - - - - - - - - - - ##
## - - - - - - - - - - MAIN CONTAINER - - - - - - - - - - ##

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

btn_registrar = Button(window_main, text="Registar", command=panel_register)
btn_registrar.place(x=500, y=360)

btn_login = Button(window_main, text="Login", command=panel_login)
btn_login.place(x=500, y=400)


currentpanel = window_main

window.mainloop()