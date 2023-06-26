from tkinter import *
import random


def switchPlayer():

    global currentplayer

    if currentplayer == players[0]:
        currentplayer = players[1]
    else:
        currentplayer = players[0]

def next_turn(row, column):

    global currentplayer

    if board[row][column]['text'] == "" and checkWin() is False:

        if currentplayer == players[0]:

            board[row][column]['text'] = currentplayer

            if checkWin() is False:
                switchPlayer()
                label.config(text=(players[1]+"'s turn"))

            elif checkWin() is True:
                label.config(text=(players[0]+" wins"))

            elif checkWin() == "Tie":
                label.config(text="Tie!")

        else:

            board[row][column]['text'] = currentplayer

            if checkWin() is False:
                switchPlayer()
                label.config(text=(players[0]+"'s turn"))

            elif checkWin() is True:
                label.config(text=(players[1]+" wins"))

            elif checkWin() == "Tie":
                label.config(text="Tie!")

def checkWin():
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":
            board[row][0].config(bg='#A4D666')
            board[row][1].config(bg='#A4D666')
            board[row][2].config(bg='#A4D666')
            return True
    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
            board[0][col].config(bg='#A4D666')
            board[1][col].config(bg='#A4D666')
            board[2][col].config(bg='#A4D666')
            return True
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        board[0][0].config(bg='#A4D666')
        board[1][1].config(bg='#A4D666')
        board[2][2].config(bg='#A4D666')
        return True
    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        board[0][2].config(bg='#A4D666')
        board[1][1].config(bg='#A4D666')
        board[2][0].config(bg='#A4D666')
        return True
    elif checkIfEmpty() is False:
        for row in range(3):
            for col in range(3):
                board[row][col].config(bg="#FEFE9A")
        return "Tie"
    else:
        return False


def checkIfEmpty():
    empty_spaces = 9

    for row in range(3):
        for col in range(3):
            if board[row][col]['text'] != "":
                empty_spaces -= 1
    if empty_spaces == 0:
        return False
    else:
        return True


def new_game():
    pass


window = Tk()
window.configure(bg="#DFF3FB")
window.title("Tic-Tac-Toe")
players = ["X", "O"]
currentplayer = random.choice(players)
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

label = Label(text=currentplayer +"'s " + "turn", font=('garamond', 40), bg="#DFF3FB")
label.pack(side="top")

reset_game = Button(text="restart", font=('capitolina', 20), background="#69C0E2")
reset_game.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        board[row][col] = Button(frame, text="", font=('garamond',40),
                                 width=5, height=2, command=lambda row=row, column=col: next_turn(row, column))
        board[row][col].grid(row=row, column=col)

window.mainloop()


