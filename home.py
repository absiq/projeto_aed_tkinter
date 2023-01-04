from tkinter import *

home_page = Tk()
home_page.title("   Home page")  
home_page.resizable(0,0)

#  pega info da dimensao da tela do usuario
widthTela = home_page.winfo_screenwidth()
heightTela = home_page.winfo_screenheight()

#define dimensao da app
appWidth = 1080
appHeigth = 720

#define as posicoes X e Y na qual a app irá aparecer na tela do usuário
posX = (widthTela/2) - (appWidth/2) 
posY = (heightTela/2) - (appHeigth/2)

home_page.geometry(f"{appWidth}x{appHeigth}+{int(posX)}+{int(posY)}")

# define icone no início da página
home_page.iconbitmap("./images/music.ico")

#define cor de fundo da home page
home_page.configure(bg = "#d3d3d3")

#coloca título da app
lblTitulo = Label(home_page, text = "Songsy", fg = "black", bg = "#d3d3d3", font = "Arial, 25",relief = "flat")
lblTitulo.place (x=500, y=5)

#define icone da lupa no botao de busca
imgSearch = PhotoImage(file = "./images/search (2).png", height=20, width=20)
btnGuardarS = Button (home_page, width = 40, height = 40, image = imgSearch, border=0, bg="#d3d3d3")
btnGuardarS.place (x = 1020 , y = 7)

#define icone de user no botao para ir p/ página do usuário
imgUser = PhotoImage(file = "./images/user (1).png", height=20, width=20)
btnGuardarU = Button (home_page, width = 40, height = 40, image = imgUser, border=0, bg="#d3d3d3")
btnGuardarU.place (x = 975 , y = 9)

#define icone de sino para ir pra página de notificações
imgNotific = PhotoImage(file = "./images/sino (1).png", height=20, width=20)
btnGuardarN = Button (home_page, width = 40, height = 40, image = imgNotific, border=0, bg="#d3d3d3")
btnGuardarN.place (x = 930 , y = 9)




home_page.mainloop()

