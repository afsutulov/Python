#!/usr/bin/python3

import random

# Функция ввода числа с проверкой
def Num(txt, n1, n2):
    if n1 > n2: n1, n2 = n2, n1
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

def Zad1(a, b):
    print('\n\tСправочник:')
    for _ in range(len(a)): print (f'ID = {a[_]:3}\tPHONE = {b[_]}')

def Zad2(a, b):
    print('\n\tКниги:')
    for _ in range(len(a)): print (f'{a[_]:20}\tГод: {b[_]}')

def Sort(a, b, Flag):
    for i in range(len(a)):
       for j in range(i, len(a)):
          if Flag:
             if a[i] > a[j]: a[i], a[j] = a[j], a[i]; b[i], b[j] = b[j], b[i]
          else:
             if b[i] > b[j]: a[i], a[j] = a[j], a[i]; b[i], b[j] = b[j], b[i]

# Задание 1
idcode = [random.randint(1, 99) for i in range(10)]
phone = [random.randint(600000, 609999) for i in range(10)]
print('ЗАДАНИЕ 1: Написать программу «справочник». Создать два списка целых. Один список хранит идентификационные коды, второй — телефонные номера. Реализовать меню для пользователя:Отсортировать по идентификационным кодам;\n - Отсортировать по номерам телефона;\n - Вывести список пользователей с кодами и телефонами;\n - Выход.\n\nРЕШЕНИЕ:')
Zad1(idcode, phone)
match Num('\nВарианты:\n\t1 - отсортировать по ID\n\t2 - отсортировать по PHINE\n\t3 - Вывести изначальный список\n\t0 - Выход\nВыберите дейстие', 0, 3):
    case 1: Sort(idcode, phone, True); Zad1(idcode, phone)
    case 2: Sort(idcode, phone, False); Zad1(idcode, phone)
    case 3: Zad1(idcode, phone)

# Задание 2
print('\n\nЗАДАНИЕ 2: Написать программу «книги». Создать два списка годы выпуска. Реализовать меню для пользователя:\n - Отсортировать по названию книг;\n - Отсортировать по годам выпуска;\n - Вывести список книг с названиями и годами выпуска;\n - Выход\n\nРЕШЕНИЕ:')
kniga = ['Укурки', 'Пермские нарколыги', 'Курим шмаль', 'Мысли наркомана', 'Курить или не курить', 'Дурь в башке', 'Лучше бы пил', 'Горе от ЗОЖ', 'Пил и буду пить', 'Шмаль forever!']
god = [random.randint(1970, 2024) for i in range(10)]
Zad2(kniga, god)
match Num('\nВарианты:\n\t1 - отсортировать по названию\n\t2 - отсортировать по году\n\t3 - Вывести изначальный список\n\t0 - Выход\nВыберите дейстие', 0, 3):
    case 1: Sort(kniga, god, True); Zad2(kniga, god)
    case 2: Sort(kniga, god, False); Zad2(kniga, god)
    case 3: Zad2(kniga, god)
