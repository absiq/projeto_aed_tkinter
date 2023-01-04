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

#define area de destaques
frameDestaques = LabelFrame (home_page, text = "   Albuns em destaque:   ", width= 800, height=350, bg="#d3d3d3", font="Arial, 10", fg= "black")
frameDestaques.place (x=140, y=80)

#define os 3 albuns destacados cada um levando a pagina do album quando clicado
            # !!!    falta colocar o comando pra ir pra pag de cada album    !!!
imgAlbum1 = PhotoImage(file = "./images/harrys-house.png", height= 200, width= 200)
btnGuardarA1 = Button (home_page, width = 200, height = 200, image = imgAlbum1, border=0, bg="#d3d3d3")
btnGuardarA1.place (x = 190 , y = 135)
tituloA1 = Label(home_page, text="Harry's House \n by Harry Styles \n POP", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
tituloA1.place(x=210, y=345)

imgAlbum2 = PhotoImage(file = "./images/divine-feminine.png", height= 200, width= 200)
btnGuardarA2 = Button (home_page, width = 200, height = 200, image = imgAlbum2, border=0, bg="#d3d3d3")   #30px de distancia entre cada album
btnGuardarA2.place (x = 430 , y = 135)
tituloA2 = Label(home_page, text="The divine feminine \n by Mac Miller \n HIP-HOP", width=24, height=3, bd=0, bg="#d3d3d3", fg="black")
tituloA2.place(x=450, y=345)

imgAlbum3 = PhotoImage(file = "./images/born-pink.png", height= 200, width= 200)
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

