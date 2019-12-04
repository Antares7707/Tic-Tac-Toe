"""
This is a Tic Tac Toe game written in Python. 
Start the game, 
and decide between you and your friend about who should be the first player. 
Take turns to place "X" or "O" by clicking on the grids as you wish. 
When one player wins or if the game end in a tie,a message box will pop up. 
Click the "OK" button on the message box to exit the game.
"""

from Tkinter import *
import tkMessageBox
root = Tk()

root.title("TIC-TAC-TOE")
root.geometry("600x500")

numturn = 1

pl1 = Label(root, text = "1st Player = X", font = "30")
pl2 = Label(root, text = "2nd Player = O", font = "30")

pl1.grid(row = 0, column = 0)
pl2.grid(row = 1, column = 0)


def clicked1():
    global numturn
    numturn += 1
    if bt1["text"] == " ":
        if (numturn%2) == 0:
            bt1["text"] = "X"
        else:
            bt1["text"] = "O"
        check()

def clicked2():
    global numturn
    numturn += 1
    if bt2["text"] == " ":
        if (numturn%2) == 0:
            bt2["text"] = "X"
        else:
            bt2["text"] = "O"
        check()

def clicked3():
    global numturn
    numturn += 1
    if bt3["text"] == " ":
        if (numturn%2) == 0:
            bt3["text"] = "X"
        else:
            bt3["text"] = "O"
        check()

def clicked4():
    global numturn
    numturn += 1
    if bt4["text"] == " ":
        if (numturn%2) == 0:
            bt4["text"] = "X"
        else:
            bt4["text"] = "O"
        check()

def clicked5():
    global numturn
    numturn += 1
    if bt5["text"] == " ":
        if (numturn%2) == 0:
            bt5["text"] = "X"
        else:
            bt5["text"] = "O"
        check()

def clicked6():
    global numturn
    numturn += 1
    if bt6["text"] == " ":
        if (numturn%2) == 0:
            bt6["text"] = "X"
        else:
            bt6["text"] = "O"
        check()

def clicked7():
    global numturn
    numturn += 1
    if bt7["text"] == " ":
        if (numturn%2) == 0:
            bt7["text"] = "X"
        else:
            bt7["text"] = "O"
        check()

def clicked8():
    global numturn
    numturn += 1
    if bt8["text"] == " ":
        if (numturn%2) == 0:
            bt8["text"] = "X"
        else:
            bt8["text"] = "O"
        check()

def clicked9():
    global numturn
    numturn += 1
    if bt9["text"] == " ":
        if (numturn%2) == 0:
            bt9["text"] = "X"
        else:
            bt9["text"] = "O"
        check()

def check():
    b1 = bt1["text"]
    b2 = bt2["text"]
    b3 = bt3["text"]
    b4 = bt4["text"]
    b5 = bt5["text"]
    b6 = bt6["text"]
    b7 = bt7["text"]
    b8 = bt8["text"]
    b9 = bt9["text"]
    if b1 == b2 and b2 == b3 and b1 == "X" or b1 == b2 and b2 == b3 and b1 == "O":
        end(b1)
    if b5 == b4 and b6 == b5 and b5 == "X" or b5 == b4 and b6 == b5 and b5 == "O":
        end(b5)
    if b7 == b8 and b8 == b9 and b9 == "X" or b7 == b8 and b8 == b9 and b9 == "O":
        end(b7)
    if b1 == b4 and b4 == b7 and b7 == "X" or b1 == b4 and b4 == b7 and b7 == "O":
        end(b1)
    if b2 == b5 and b5 == b8 and b8 == "X" or b2 == b5 and b5 == b8 and b8 == "O":
        end(b2)
    if b3 == b6 and b6 == b9 and b9 == "X" or b3 == b6 and b6 == b9 and b9 == "O":
        end(b3)
    if b1 == b5 and b5 == b9 and b9 == "X" or b1 == b5 and b5 == b9 and b9 == "O":
        end(b1)
    if b3 == b5 and b5 == b7 and b7 == "X" or b3 == b5 and b5 == b7 and b7 == "O":
        end(b3)
    if numturn == 10:
        tkMessageBox.showinfo("TIC-TAC-TOE","This is a tie....")

def end(ox):
    if ox == "X":
        winner = "Player 1"
    if ox == "O":
        winner = "Player 2"
    tkMessageBox.showinfo("TIC-TAC-TOE","Congratulations "+winner+"!!! You have won!!")
    root.destroy()
    



bt1 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked1)
bt1.grid(row = 2, column = 4)
bt2 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked2)
bt2.grid(row = 2, column = 5)
bt3 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked3)
bt3.grid(row = 2, column = 6)
bt4 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked4)
bt4.grid(row = 3, column = 4)
bt5 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked5)
bt5.grid(row = 3, column = 5)
bt6 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked6)
bt6.grid(row = 3, column = 6)
bt7 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked7)
bt7.grid(row = 4, column = 4)
bt8 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked8)
bt8.grid(row = 4, column = 5)
bt9 = Button(root, text = " ", width = 10, height = 5, fg = "White", bg = "Black", font = "100", command = clicked9)
bt9.grid(row = 4, column = 6)


root.mainloop()
