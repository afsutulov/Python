#!/usr/bin/python3


from tkinter import *
from tkinter import messagebox

Player = 'X'
stop_game = False

def clicked(r, c):
    pass

b = [[0,0,0], [0,0,0], [0,0,0]]
states = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(height=4, width=8, font=("Helvetica", 20), command = lambda r = i, c = j:clicked(r,c) )
    b[i][j].grid(row=i, column=j)

root = Tk()
root.title("Крестики - Нолики")
mainloop()
