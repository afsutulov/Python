#!/usr/bin/python3

import tkinter as tk
from tkinter import scrolledtext
from tkinter.messagebox import askyesno
import random, sys, os

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Морской бой")
        icon = tk.PhotoImage(file=self.resource_path("boy.png"))
        root.iconphoto(True, icon)
        self.clr = ["#6198f6", "#ffffff", "#2d55e4", "#c7d8f7", "#dddddd", "#f8604a", "#0077ff", "#3cb371"]
        self.root.configure(bg=self.clr[0])
        # Запретить изменение размеров окна
        self.root.resizable(False, False)
        # Заголовки над игровыми полями
        self.p1_label = tk.Label(root, text="поле Игрока", fg=self.clr[1], bg=self.clr[0], font=("Arial", 12, "bold"))
        self.p1_label.grid(row=0, column=0, pady=(10, 0))
        self.p2_label = tk.Label(root, text="поле Противника", fg=self.clr[1], bg=self.clr[0], font=("Arial", 12, "bold"))
        self.p2_label.grid(row=0, column=1, pady=(10, 0))
        # Рамки для полей
        self.left_frame = tk.Frame(root)
        self.left_frame.grid(row=1, column=0, padx=10, pady=10)
        self.right_frame = tk.Frame(root)
        self.right_frame.grid(row=1, column=1, padx=10, pady=10)
        # Создаём поля с подписями
        self.b1 = self.CreateButtons(self.left_frame)
        self.b2 = self.CreateButtons(self.right_frame)
        # Кнопка "Начать игру" по центру
        self.button_frame = tk.Frame(root, bg=self.clr[0])
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        self.start_button = tk.Button(self.button_frame, text="Начать игру", command=self.Start, relief="flat", fg=self.clr[2], bg=self.clr[3], activeforeground=self.clr[1], activebackground=self.clr[2], width=20)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.exit_button = tk.Button(self.button_frame, text="Выход", command=root.destroy, relief="flat", fg=self.clr[2], bg=self.clr[3], activeforeground=self.clr[1], activebackground=self.clr[2], width=20)
        self.exit_button.pack(side=tk.LEFT, padx=10)
        # Лог игры под обоими полями
        self.log_text = scrolledtext.ScrolledText(root, width=90, height=10, state='normal', bg=self.clr[1])
        self.log_text.grid(row=3, column=0, columnspan=2, pady=10)
        self.Log("Для начала игры нажмите кнопку \"Начать игру\"...")
        self.p1 = []
        self.p2 = []
        self.hod = []

    # Для добавления иконки в исполняемый файл
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    # Создаем кнопки Поля
    def CreateButtons(self, parent):
        field_frame = tk.Frame(parent, bg=self.clr[2], padx=0, pady=0)
        field_frame.pack()
        buttons = []
        for i in range(12):
            row = []
            for j in range(12):
                if (i == 0 or i == 11) and (j > 0 and j < 11):
                    label = tk.Label(field_frame, text=chr(64 + j), width=2, fg=self.clr[1], bg=self.clr[2])
                    label.grid(row=i, column=j)
                elif (j == 0 or j == 11) and (i > 0 and i < 11):
                    label = tk.Label(field_frame, text=str(i), width=2, fg=self.clr[1], bg=self.clr[2])
                    label.grid(row=i, column=j)
                elif (i > 0 and i < 11) and (j > 0 and j < 11):
                    btn = tk.Button(field_frame, width=2, height=1, bg=self.clr[1], relief="ridge")
                    btn.grid(row=i, column=j)
                    row.append(btn)
            if row: buttons.append(row)
        return buttons

    # Выдаем сообщения в лог игры
    def Log(self, txt):
        self.log_text.insert(tk.END, f"{txt}\n")
        self.log_text.yview(tk.END)

    # Заполняем поле 10x10 фигурами
    def SetPole(self, a):
        for z in range(4, 0, -1): # Цикл по фигурам: от 4х келочных до 1на клеточных
            for _ in range(5 - z): # Цикл по количеству фигур в зависимости от количества клеток в фигуре
                while True: # Цикл создания фигуры
                    Flag2 = random.getrandbits(1) # Случайное направление размещения фигуры: True - горизонтальное, False - вертикальное
                    if Flag2: x = random.randint(1, 10); y = random.randint(1, 11 - z)
                    else: x = random.randint(1, 11 - z); y = random.randint(1, 10)
                    Flag = True
                    if Flag2:
                        for i in range(x - 1, x + 2): # Проверяем нет ли вокруг другой фигуры
                            for j in range(y - 1, y + 1 + z):
                                if a[i][j] == '#': Flag = False
                        if Flag: # Если фигур нет - создаем фигуру и выходим из цикла
                            for w in range(z): a[x][y + w] = '#';
                            break
                    else:
                        for i in range(x - 1, x + 1 + z): # Проверяем нет ли вокруг другой фигуры
                            for j in range(y - 1, y + 2):
                                if a[i][j] == '#': Flag = False
                        if Flag: # Если фигур нет - создаем фигуру и выходим из цикла
                            for w in range(z): a[x + w][y] = '#';
                            break

    # Обновляем поля игроков с учетом изменений в игре
    def ShowPole(self):
        for i in range(10):
            for j in range(10):
                match self.p1[i + 1][j + 1]:
                    case "#": self.b1[i][j].configure(bg=self.clr[0], state=["disable"])
                    case "X": self.b1[i][j].configure(bg=self.clr[5], state=["disable"])
                    case "o": self.b1[i][j].configure(bg=self.clr[4], state=["disable"])
                    case _: self.b1[i][j].configure(bg=self.clr[1], state=["disable"])
                match self.p2[i + 1][j + 1]:
                    case "X": self.b2[i][j].configure(bg=self.clr[7], state=["disable"])
                    case "o": self.b2[i][j].configure(bg=self.clr[4], state=["disable"])
                    case _: self.b2[i][j].configure(bg=self.clr[1], state=["normal"])

    # Начало игры по кнопке. Расставляем фигуры. Отчищаем лог
    def Start(self):
        self.p1 = [[' ' for _ in range(12)] for _ in range(12)] # Поле игрока (12x12)
        self.p2 = [[' ' for _ in range(12)] for _ in range(12)] # Поле противника (12x12)
        self.hod = [] # Список будущих ходов для ИИ
        self.SetPole(self.p1)
        self.SetPole(self.p2)
        for i in range(10):
            for j in range(10): self.b2[i][j].configure(command = lambda r = i + 1, c = j + 1:self.Hod(r, c))
        for i in range(len(self.p1)):
            for j in range(len(self.p1)):
                if i == 0 or j == 0 or i == len(self.p1) - 1 or j == len(self.p1) - 1: self.p1[i][j] = "-" # Заполняем края "-" - ИИ не рассматривает их для будущих ходов

        self.ShowPole()
        self.log_text.delete(1.0, tk.END)
        self.Log("Начинаем игру!\nХод Игрока")

    # Возвращаем поражение Игрока либо Противника
    def Porajenie(self, a):
        Flag = True
        for _ in range(len(a)):
            if "#" in a[_]: Flag = False
        return Flag

    # Проверка завершения игры
    def Game_off(self):
        txt = ""
        if self.Porajenie(self.p2): txt = "Игрок"
        elif self.Porajenie(self.p1): txt = "Противник"
        if txt !="":
            self.Log(f"Победил {txt}! Игра окончена");
            if askyesno(title="Игра окончена!", message=f"Победил {txt}!\nСыграем еще?"): self.Start()
            else: root.destroy()

    # Игрок делает Ход (по кнопке). Далее обрабатываем ходы Противника
    def Hod(self, x, y):
        Flag = True
        match self.p2[x][y]:
            case "#": self.p2[x][y] = "X"; self.Log(f"Игрок: Ход {chr(64 + y)}{x}. Подбил цель!"); Flag = False
            case " ": self.p2[x][y] = "o"; self.Log(f"Игрок: Ход {chr(64 + y)}{x}. Мимо!")
        self.ShowPole()
        self.Game_off()
        if Flag: self.Log("Переход хода Противнику")
        while Flag:
            if not self.hod: # Если список ходов ИИ пуст, стреляем в случайную клетку исключая повтор и рядом с известной фигурой
                while True:
                    x = random.randint(1, 10)
                    y = random.randint(1, 10)
                    if self.p1[x][y] != "-" and self.p1[x][y] != "o": break
            else: # Если есть список ходов ИИ не пуст - делаем ход и удаляем его из списка
                x = self.hod[0][0]
                y = self.hod[0][1]
                self.hod.pop(0)
            match self.p1[x][y]:
                case "#":
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            if self.p1[i][j] != "-" and self.p1[i][j] != "X" and ((i == x and j != y) or (j == y and i != x)): self.hod.append([i, j]) # Проверяем соседа на возможность хода. Если ок - добавляем в список ходов ИИ
                            if self.p1[i][j] == " ": self.p1[i][j] = "-" # Заполняем область вокруг исключениям, чтобы туда не стрелять (только если точка в списке ходов ИИ)
                    self.p1[x][y] = "X"; # Саму координату помечаем как "подбит"
                    self.Log(f"Противник: Ход {chr(64 + y)}{x}. Подбил цель!")
                case " " | "-": self.p1[x][y] = "o"; self.Log(f"Противник: Ход {chr(64 + y)}{x}. Мимо!\nПереход хода Игроку"); Flag = False # Выход из цикла - переход хода на Игрока
            self.ShowPole()
            self.Game_off()

if __name__ == "__main__":
    root = tk.Tk()
    app = Game(root)
    root.mainloop()
