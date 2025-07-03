#!/usr/bin/python3

import random

player = 0
p1 = [[' ' for _ in range(12)] for _ in range(12)] # Поле игрока (12x12)
p2 = [[' ' for _ in range(12)] for _ in range(12)] # Поле противника (12x12)

# Заполняем поле 10x10 фигурами
def SetPole(a):
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

# Выводим поле на экран
def Pole():
    print(f"\033[H\033[2JИгра \"Морской бой\"!\n\n  {'ИГРОК':^20}  {'ПРОТИВНИК':^20}\n ", end="")
    for _ in range(10): print(f" {_}", end="")
    print(" "*2, end="")
    for _ in range(10): print(f" {_}", end="")
    print(f"\n  {'-'*20}  {'-'*20}")
    for i in range(1, 11):
        txt = f"{i-1}|"
        for j in range(1, 11): txt += f"{p1[i][j]}|"
        txt = txt.replace("#", "\033[47m \033[0m").replace("X", "\033[41m \033[0m")
        txt2 = f"{i-1}|"
        for j in range(1, 11): txt2 += f"{p2[i][j]}|"
        txt2 = txt2.replace("X", "\033[42m \033[0m")
        print(f"{txt}{txt2.replace('#', ' ')}{i-1}\n  {'-'*20}  {'-'*20}")
    print(" ", end="")
    for _ in range(10): print(f" {_}", end="")
    print(" "*2, end="")
    for _ in range(10): print(f" {_}", end="")
    print("\n")

# Функция ввода числа с проверкой
def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

# Ведение лога
def Log(txt):
    _ = input(txt)
    with open('log.txt', 'a') as f: f.write(f"{txt}\n")

# Обрабатываем ход игрока
def Igrok():
    global player
    Flag = True
    while Flag:
        x = Num("Введите значение хода по вертикали", 0, 9)
        y = Num("Введите значение хода по горизонтали", 0, 9)
        match p2[x + 1][y + 1]:
            case "#": p2[x + 1][y + 1] = "X"; Log(f"Игрок: Ход {x}x{y}. Подбил цель!"); Flag = False
            case " ": p2[x + 1][y + 1] = "o"; Log(f"Игрок: Ход {x}x{y}. Мимо!"); Flag = False; player = 1 - player

# Делает ход противник
def Protivnik():
    global player
    Flag = True
    while Flag:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        match p1[x + 1][y + 1]:
            case "#": p1[x + 1][y + 1] = "X"; Log(f"Противник: Ход {x}x{y}. Подбил цель!"); Flag = False
            case " ": p1[x + 1][y + 1] = "o"; Log(f"Противник: Ход {x}x{y}. Мимо!"); Flag = False; player = 1 - player

# Возвращаем поражение Игрока либо Противника
def Porajenie(a):
    Flag = True
    for _ in range(len(a)):
        if "#" in a[_]: Flag = False
    return Flag

# Проверка завершения игры
def Game_off():
    if Porajenie(p2): Log("Победил Игрок! Игра окончена"); exit()
    elif Porajenie(p1): Log("Победил Противник! Игра окончена"); exit()

# Игровой процесс
def game():
    global player
    SetPole(p1)
    SetPole(p2)
    with open('log.txt', 'w') as f: f.write("Начинаем игру!")
    while True:
        Pole()
        if player == 0: Igrok()
        else: Protivnik()
        Game_off()

if __name__ == "__main__": game()