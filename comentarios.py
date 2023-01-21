from tkinter import *
import os


window = Tk()
window.geometry('1080x720')
window.title('Comentários')

userFile  = "databases\currentsession.csv"
commentsFile = "comentarios.txt"

f = open(userFile, "r", encoding="utf-8")
users = f.readlines()
f.close()
for user in users:
    user = user.split(",")
    userName = user[3]


comments = Text(window, width=40, height=10)
comments.place(x = 10, y = 50)

def read_comments():
    if os.path.exists(commentsFile):
        f = open(commentsFile, "r", encoding="utf-8")
        comments_data = f.readlines()
        for comment in comments_data:
            comm = comment.split(";")
            for com in comm:
                print(com)
                comments.insert(INSERT, com[1] + ": " + com[2] + "\n")
    else:
        comments.insert(INSERT, "No comments yet")


def add_comment(userName):
    comment = comment_entry.get()
    comments.insert(INSERT, userName + ": " + comment + "\n")
    writeComment(comment)

def writeComment(comment):
    fComent = open(commentsFile, "a")
    
    fComent.write(comment)
    fComent.close()


comment_label = Label(window, text="Comentário:")
comment_label.place(x = 10, y = 10)
comment_entry = Entry(window)
comment_entry.place(x = 80, y = 10)

add_comment_button = Button(window, text="Comentar", command= lambda: (add_comment(userName)))
add_comment_button.place(x = 250, y = 10)

read_comments()

window.mainloop()