#!/usr/bin/python3

import tkinter as tk
#from tkinter import messagebox

root = tk.Tk()
root.geometry("250x250")

root.title("Крестики - Нолики")

FrameOne = tk.Frame()
FrameTwo = tk.Frame()

#Label - надпись на экране
label = tk.Label(master=FrameOne, text="Первое приложение", foreground="white", background="black", font=("Roboto", 12))
label.pack()

#Button - кнопка
button = tk.Button(master=FrameOne, text="Нажми меня", width=25, height=5, fg="green", bg="red")
button.pack()

#Entry - поле ввода
labelName = tk.Label(master=FrameTwo, text="Имя")
labelName.pack()

entry = tk.Entry(master=FrameTwo)
entry.pack()
#entry.delete(0, tk.END)
#entry.insert(0, "ИВАН")
#entry.get()

#Text - большое поле для текста

#Frame - окно для группировки объекта

FrameTwo.pack()
FrameOne.pack()

tk.mainloop()
