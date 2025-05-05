#!/usr/bin/python3

import random

def factorial(n):
    if n == 1 : return 1
    else: return n * factorial(n-1)

#print(factorial(6))

# Рекурсивная функция для нахождения степени числа
def kvad(a, n):
    if n == 0: return 1
    else: return a * kvad(a, n - 1)

#print(kvad(int(input('Цифра 1: ')), int(input('Цифра 2: '))))


# Функция вычисляет сумму элементов между а и б
def summa(a, b):
    if a == b: return b
    else: return a + summa(a + 1, b)

#print(summa(int(input('Цифра 1: ')), int(input('Цифра 2: '))))


# Функция, которая выводит N звеpз в ряд
def zvezda(x):
    if x == 0: return ''
    else: return '*' + zvezda(x - 1)

#print(zvezda(int(input('ВВедиче количество x: '))))


# Функция, которая принимает список из 100 случайных элементов, находит позицию с которой начинается последовательность из 10 чисел, сумма которых минимальная
mass = []
mins = []
while len(mass) < 100: mass.append(random.randint(0, 100))

def Summa(x):
    if x == 90: print(f'\nМассив: {mass}\nМинимальная сумма 10 последовательных цифр: {min(mins)}\nПозиция: {mins.index(min(mins))}')
    else: mins.append(sum(mass[x:x + 10])); Summa(x + 1)

if __name__ == '__main__': Summa(0)
