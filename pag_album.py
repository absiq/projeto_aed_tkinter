from tkinter import *

ficheiro = "pop.txt"

window=Tk()
window.geometry("500x500")
window.title("Álbum")
window.resizable(0,0)

ctnImage = Canvas(window, width=190, height=190, bd=2, relief="sunken")
ctnImage.place(x=20, y=20)

f = open(ficheiro, "r", encoding="utf-8")
linhas = f.readlines()
f.close()
for linha in linhas:
    campos = linha.split(";")
    if campos[0] == "1":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "2":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "3":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "4":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "5":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "6":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "7":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "8":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "9":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "10":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "11":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black")
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
    elif campos[0] == "12":
        img = PhotoImage(file = campos[1])
        album_name = Label(window, text=campos[2], fg="black", font=('Arial', 80))
        album_artist = Label(window, text=campos[3], fg="black", font=('Arial', 16))
        album_info = Label(window, text=campos[4] + ", " + campos[5] + ", " + campos[6] + ", " + campos[7], fg="black")
        album_description = Label(window, text=campos[9], fg="black", wraplength=450, justify="left")
        album_score = Label(window, text=campos[8], fg="black")
        songs = Label(window, text=campos[11], fg="black")

ctnImage.create_image(100, 100, image = img) 
album_name.place(x=250,y=60)
album_artist.place(x=250,y=170)
album_info.place(x=250,y=199)
album_description.place(x = 20, y = 270)
album_score.place(x=170, y=220)
songs.place(x=20,y=350)



share_btn= PhotoImage(file="share-icon.png")
share_label= Label(image=share_btn)
button_share= Button(window, relief = "raised", image=share_btn, borderwidth=0)
button_share.place(x = 20, y = 220)

like_btn= PhotoImage(file="heart-icon.png")
like_label= Label(image=like_btn)
button_like= Button(window, relief = "raised", image=like_btn, borderwidth=0)
button_like.place(x = 80, y = 220)

stars_btn= PhotoImage(file="star-icon.png")
stars_label= Label(image=stars_btn)
button_stars= Button(window, image=stars_btn, borderwidth=0)
button_stars.place(x = 250, y = 220)

stars_btn2= PhotoImage(file="star-icon.png")
stars_label2= Label(image=stars_btn2)
button_stars2= Button(window, image=stars_btn2, borderwidth=0)
button_stars2.place(x = 285, y = 220)

stars_btn3= PhotoImage(file="star-icon.png")
stars_label3= Label(image=stars_btn3)
button_stars3= Button(window, image=stars_btn3, borderwidth=0)
button_stars3.place(x = 320, y = 220)

stars_btn4= PhotoImage(file="star-icon.png")
stars_label4= Label(image=stars_btn4)
button_stars4= Button(window, image=stars_btn4, borderwidth=0)
button_stars4.place(x = 355, y = 220)

stars_btn5= PhotoImage(file="star-icon.png")
stars_label5= Label(image=stars_btn5)
button_stars5= Button(window, image=stars_btn5, borderwidth=0)
button_stars5.place(x = 390, y = 220)

window.mainloop() 