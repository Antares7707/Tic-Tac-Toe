from tkinter import *
from tkinter import messagebox
root = Tk()

root.title("TIC-TAC-TOE")
root.geometry("600x500")

numturn = 1

pl1 = Label(root, text = "You = O", font = "30")
pl2 = Label(root, text = "Computer = X", font = "30")

pl1.grid(row = 0, column = 0)
pl2.grid(row = 1, column = 0)


def clicked1():
    global numturn
    if bt1["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt1["text"] = "O"
        check()

def clicked2():
    global numturn
    if bt2["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt2["text"] = "O"
        check()

def clicked3():
    global numturn
    if bt3["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt3["text"] = "O"
        check()

def clicked4():
    global numturn
    if bt4["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt4["text"] = "O"
        check()

def clicked5():
    global numturn
    if bt5["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt5["text"] = "O"
        check()

def clicked6():
    global numturn
    if bt6["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt6["text"] = "O"
        check()

def clicked7():
    global numturn
    if bt7["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt7["text"] = "O"
        check()

def clicked8():
    global numturn
    if bt8["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt8["text"] = "O"
        check()

def clicked9():
    global numturn
    if bt9["text"] == " ":
        numturn += 1
        if (numturn%2) == 0:
            bt9["text"] = "O"
        check()

def check():
    gameover = 0
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
        gameover+=1
    if b5 == b4 and b6 == b5 and b5 == "X" or b5 == b4 and b6 == b5 and b5 == "O":
        end(b5)
        gameover+=1
    if b7 == b8 and b8 == b9 and b9 == "X" or b7 == b8 and b8 == b9 and b9 == "O":
        end(b7)
        gameover+=1
    if b1 == b4 and b4 == b7 and b7 == "X" or b1 == b4 and b4 == b7 and b7 == "O":
        end(b1)
        gameover+=1
    if b2 == b5 and b5 == b8 and b8 == "X" or b2 == b5 and b5 == b8 and b8 == "O":
        end(b2)
        gameover+=1
    if b3 == b6 and b6 == b9 and b9 == "X" or b3 == b6 and b6 == b9 and b9 == "O":
        end(b3)
        gameover+=1
    if b1 == b5 and b5 == b9 and b9 == "X" or b1 == b5 and b5 == b9 and b9 == "O":
        end(b1)
        gameover+=1
    if b3 == b5 and b5 == b7 and b7 == "X" or b3 == b5 and b5 == b7 and b7 == "O":
        end(b3)
        gameover+=1
    if numturn == 10:
        messagebox.showinfo("TIC-TAC-TOE","This is a tie....")
        root.destroy()
        gameover+=1
    if gameover == 0:
        if numturn%2 == 0:
            ai()


def ai():
    global numturn
    numturn += 1
    stra = 0
    b1 = bt1["text"]
    b2 = bt2["text"]
    b3 = bt3["text"]
    b4 = bt4["text"]
    b5 = bt5["text"]
    b6 = bt6["text"]
    b7 = bt7["text"]
    b8 = bt8["text"]
    b9 = bt9["text"]
    if stra == 0:
        if (b1 == b2 == "O" or b1 == b2 == "X") and b3 == " ":
            bt3["text"] = "X"
            stra+=1
            check()
    if stra == 0:
        if (b3 == b2 == "O" or b3 == b2 == "X") and b1 == " ":
            bt1["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b1 == b4 == "O" or b1 == b4 == "X") and b7 == " ":
            bt7["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b7 == b4 == "O" or b7 == b4 == "X") and b1 == " ":
            bt1["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b1 == b5 == "O" or b1 == b5 == "X") and b9 == " ":
            bt9["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b9 == b5 == "O" or b9 == b5 == "X") and b1 == " ":
            bt1["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b2 == b5 == "O" or b2 == b5 == "X") and b8 == " ":
            bt8["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b8 == b5 == "O" or b8 == b5 == "X") and b1 == " ":
            bt1["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b3 == b6 == "O" or b3 == b6 == "X") and b9 == " ":
            bt9["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b9 == b6 == "O" or b9 == b6 == "X") and b3 == " ":
            bt3["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b3 == b5 == "O" or b3 == b5 == "X") and b7 == " ":
            bt7["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b7 == b5 == "O" or b7 == b5 == "X") and b3 == " ":
            bt3["text"] = "X"
            check()
            stra+=1
            stra+=1
    if stra == 0:
        if (b4 == b5 == "O" or b4 == b5 == "X") and b6 == " ":
            bt6["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b6 == b5 == "O" or b6 == b5 == "X") and b4 == " ":
            bt4["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b7 == b8 == "O" or b7 == b8 == "X") and b9 == "":
            bt9["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b9 == b8 == "O" or b9 == b8 == "X") and b7 == " ":
            bt7["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b1 == b3 == "O" or b1 == b3 == "X") and b2 == " ":
            bt2["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b1 == b7 == "O" or b1 == b7 == "X") and b4 == " ":        
            bt4["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b3 == b9 == "O" or b9 == b3 == "X") and b6 == " ":
            bt6["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if (b9 == b7 == "O" or b9 == b7 == "X") and b8 == " ":
            bt8["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        if b5 == " ":
            bt5["text"] = "X"
            check()
            stra+=1
    if stra == 0:
        gridlist = [bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9]
        for i in gridlist:
            if i["text"] == " ":
                i["text"] = "X"
                break
        check()


def end(ox):
    if ox == "X":
        result = "The Computer has won!!!"
    if ox == "O":
        result = "Congratulations!!! You have won!!"
    messagebox.showinfo("TIC-TAC-TOE",result)
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

