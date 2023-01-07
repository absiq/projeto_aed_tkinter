from tkinter import *
from users import *
from os import *

painel_adm = Tk()
painel_adm.title(" Painel do administrador")  
painel_adm.resizable(0,0)

#  pega info da dimensao da tela do usuario
widthTela = painel_adm.winfo_screenwidth()
heightTela = painel_adm.winfo_screenheight()

#define dimensao da app
appWidth = 1080
appHeigth = 720

#define as posicoes X e Y na qual a app irá aparecer na tela do usuário
posX = (widthTela/2) - (appWidth/2) 
posY = (heightTela/2) - (appHeigth/2)

painel_adm.geometry(f"{appWidth}x{appHeigth}+{int(posX)}+{int(posY)}")

# define icone no início da página
painel_adm.iconbitmap("./imgs/home/music.ico")

#define cor de fundo da home page
painel_adm.configure(bg = "#d3d3d3")

# ________________________________________________________ #

# imagem do administrador, nome e username
name, username, icon = retrieve_current_user_data()

userInfoName = "Nome: " + name
label_userInfoName = Label(painel_adm, text=userInfoName)
label_userInfoName.place(x=20, y=50)
userInfoName.place (x=420, y=400)

userInfoUsername = "Username: " + username
label_userInfoUsername = Label(painel_adm, text=userInfoName)
label_userInfoUsername.place(x=20, y=50)
userInfoUsername.place (x=420, y=480)

ficheiro_img = os.path.join('imgs\\profile_pics', icon)
user_img = Canvas(painel_adm, width=100, height=100, bd=0)
user_img.place(x=420, y=100)
global img
img = PhotoImage(file = ficheiro_img)
user_img.create_image(50,50, anchor=CENTER, image = img)

"""
userImg = PhotoImage (file= "./imgs/painel_adm/user.png")
userImg.place(x= 420, y=100)


        # canvas
lugarImg = Canvas(painel_adm, width=230, height=230, bg="#d3d3d3", border=0)
lugarImg.place(x= 420, y=100)
        #imagem inicial
imgInicio = PhotoImage (file= "./imgs/painel_adm/user.png")
image_id = lugarImg.create_image(0,0, anchor = "nw", image = imgInicio)
        #funcao edit img

#botao de editar imagem
imgEdit = PhotoImage(file = "./imgs/painel_adm/pencil.png", height= 20, width= 20)
btnEdit =  Button(painel_adm, width = 40, height = 40, image = imgEdit, border=0, bg="#d3d3d3", command = editImgAdm())
btnEdit.place (x=800, y=100) 
"""


painel_adm.mainloop()