from tkinter import *

painel_adm = Tk()
painel_adm.title(" Painel do administrador")  
painel_adm.resizable(0,0)


"""painel_adm = PanedWindow(window, width=1080, height=720)
painel_adm.place(x=0,y=0)
currentpanel = painel_adm
painel_adm.configure(bg = "#d3d3d3")"""

# imagem e infos do user
userImg = PhotoImage(file= "./imgs/painel_adm/user.png")
labelImg = Label(painel_adm, image=userImg, width=180, height=180, bd=0, bg="#d3d3d3")
labelImg.place(x= 420, y=100)



admTxt = Label(painel_adm, text="Função: administrador", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
admTxt.place(x=420, y=345)


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