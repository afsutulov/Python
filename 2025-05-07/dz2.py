#!/usr/bin/python3

import random

# Функция ввода числа с проверкой
def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

def Zad1():
    print('\n\tСправочник:')
    for _ in range(len(idcode)): print(f'ID = {idcode[_]:<4}PHONE = {phone[_]}')

def Zad2():
    print('\n\tКниги:')
    for _ in range(len(kniga)): print(f'{kniga[_]:20}\tГод: {god[_]}')

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
print('ЗАДАНИЕ 1: Написать программу «справочник». Создать два списка целых. Один список хранит идентификационные коды, второй — телефонные номера. Реализовать меню для пользователя:\n - отсортировать по идентификационным кодам;\n - Отсортировать по номерам телефона;\n - Вывести список пользователей с кодами и телефонами;\n - Выход.\n\nРЕШЕНИЕ:')
Zad1()
match Num('\nВарианты:\n\t1 - отсортировать по ID\n\t2 - отсортировать по PHONE\n\t3 - Вывести изначальный список\n\t0 - Выход\nВыберите дейстие', 0, 3):
    case 1: Sort(idcode, phone, True); Zad1()
    case 2: Sort(idcode, phone, False); Zad1()
    case 3: Zad1()

# Задание 2
print('\n\nЗАДАНИЕ 2: Написать программу «книги». Создать два списка с данными. Один список храни название книг, второй - годы выпуска. Реализовать меню для пользователя:\n - Отсортировать по названию книг;\n - Отсортировать по годам выпуска;\n - Вывести список книг с названиями и годами выпуска;\n - Выход\n\nРЕШЕНИЕ:')
kniga = ['Укурки', 'Пермские нарколыги', 'Курим шмаль', 'Мысли наркомана', 'Курить или не курить', 'Дурь в башке', 'Лучше бы пил', 'Горе от ЗОЖ', 'Пил и буду пить', 'Шмаль forever!']
god = [random.randint(1970, 2024) for i in range(10)]
Zad2()
match Num('\nВарианты:\n\t1 - отсортировать по названию\n\t2 - отсортировать по году\n\t3 - Вывести изначальный список\n\t0 - Выход\nВыберите дейстие', 0, 3):
    case 1: Sort(kniga, god, True); Zad2()
    case 2: Sort(kniga, god, False); Zad2()
    case 3: Zad2()
