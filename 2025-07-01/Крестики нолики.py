#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox

Player = 'X'
stop_game = False
b = [[0,0,0], [0,0,0], [0,0,0]]
states = [[0,0,0], [0,0,0], [0,0,0]]
root = Tk()
root.title("Крестики - Нолики")

def clicked(r, c):
    global Player
    if Player == 'X' and states[r][c] == 0 and not stop_geme: b[r][c].configure(text='X'); states[r][c] = 'X'; Player = '0'
    if Player == '0' and states[r][c] == 0 and not stop_geme: b[r][c].configure(text='0'); states[r][c] = '0'; Player = 'X'
    check_win()
    if stop_game == True: winner = messagebox.showinfo("Все!", "Игра окончена"); root.destroy()

def check_win():
    global stop_game
    txt = ""
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0: txt = f"Победил {states[i][0]}!"
        elif states[0][i] == states[1][i] == states[2][i] != 0: txt = f"Победил {states[0][i]}!"
    if states[0][0] == states[1][1] == states[2][2] != 0: txt = f"Победил {states[0][0]}!"
    elif states[2][0] == states[1][1] == states[0][2] != 0: txt = f"Победил {states[2][0]}!"
    if not 0 in states[0] and not 0 in states[1] and not 0 in states[2]: txt = "Ничья. Победителя нет!"
    if txt != "": stop_game = True; winner = messagebox.showinfo("Внимание!", txt)

def main():
    global b, states
    for i in range(3):
        for j in range(3):
            b[i][j] = Button(height=4, width=8, font=("Helvetica", 20), command = lambda r = i, c = j:clicked(r, c))
            b[i][j].grid(row=i, column=j)
    mainloop()

if __name__ == "__main__": main()