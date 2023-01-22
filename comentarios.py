from tkinter import *
import os
from users import *

name, username, icon, bio, user_id = retrieve_current_user_data()

window = Tk()
window.geometry('1080x720')
window.title('Comentários')

commentsFile = "comentarios.txt"


comments = Text(window, width=40, height=10)
comments.place(x = 10, y = 50)

alb_id = "1"

def read_comments(alb_id):
    f = open(commentsFile, 'r')
    campos = f.readlines()
    f.close()
    for line in campos:
        line_split = line.split(';')
        if line_split[0] == str(alb_id):
            comments = line_split[1]
            list_comments = comments.split(',')
            for line in list_comments:
                list_comm = line.split('-')
                user = list_comm[0]
                comment = list_comm[1]
                print(comment, user)
                comments.insert(INSERT, user + ": " + comment + "\n")
                

def create_comment(alb_id, username, comment):
    ficheiro = 'comentarios.txt'
    f = open(ficheiro, 'r', encoding="utf-8")
    campos = f.readlines()
    f.close()
    i = 0
    for line in campos:
        data = line.split(';')
        if data[0] == alb_id:
            if data[1] != "":
                new_comments = []
                usercomment = data[1].split(',')
                previous_comments = ','.join(map(str, usercomment)) 
                new_comment = "'{0}'-'{1}'" .format(username, comment)
                new_comments.insert(0, new_comment)
                list_to_string = ','.join(map(str, new_comments))
                line = alb_id + ';' + previous_comments + "," + list_to_string + ';' + "\n"
                print(line)
                campos[i] = line
                j = open(ficheiro, 'w', encoding="utf-8")
                j.writelines(campos)
                j.close()
            else:
                new_comment = "'{0}'-'{1}'" .format(username, comment)
                line = alb_id + ';' + new_comment + ';' + "\n"
                j = open(ficheiro, 'w', encoding="utf-8")
                j.writelines(campos)
                j.close()
        else:
            i += 1 


def add_comment(username):
    comment = comment_entry.get()
    comments.insert(INSERT, username + ": " + comment + "\n")
    writeComment(comment)
    create_comment(alb_id, username, comment)

def writeComment(comment):
    fComent = open(commentsFile, "a")
    fComent.write(comment)
    fComent.close()


comment_label = Label(window, text="Comentário:")
comment_label.place(x = 10, y = 10)
comment_entry = Entry(window)
comment_entry.place(x = 80, y = 10)

add_comment_button = Button(window, text="Comentar", command= lambda: (add_comment(username)))
add_comment_button.place(x = 250, y = 10)


window.mainloop()