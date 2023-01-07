from tkinter import *
from users import *
from os import *
# from main import panel_account

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

# imagem do administrador, nome, funcao e username

admTxt = Label(painel_adm, text="Função: administrador", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
admTxt = Label(painel_adm, text="Função: administrador", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
admTxt.place(x=420, y=345)

userImg = PhotoImage(file= "./imgs/painel_adm/user.png")
labelImg = Label(painel_adm, image=userImg, width=180, height=180, bd=0, bg="#d3d3d3")
labelImg.place(x= 420, y=100)

# botão voltar
btnVoltar = Button(painel_adm, text="Voltar", width=10)
btnVoltar.place(x=30, y=30)

# botão add album
btnAddAlbum = Button(painel_adm, text="Adicione um álbum", width=25)
btnAddAlbum.place(x=300, y=480)

# botão remover album
btnRemovAlbum = Button(painel_adm, text="Remova um álbum", width=25)
btnRemovAlbum.place(x=520, y=480)

# botão usuarios
btnUsers = Button(painel_adm, text="Veja usuários", width=25)
btnUsers.place(x=300, y=525)

# botão apagar reviews
btnApagarReviews = Button(painel_adm, text="Apague um review", width=25)
btnApagarReviews.place(x=520, y=525)

# botão log out
btnLogOut = Button(painel_adm, text="Log out", width=10)
btnLogOut.place(x=960, y=670)







painel_adm.mainloop()