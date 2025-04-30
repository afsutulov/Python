#!/usr/bin/python3

#import math as mt, sys
#from config import user_value
#from platform import platform, machine, processor, system, version

#print(mt.pi) # Вывод числа Pi
#print(user_value)

#for name in dir(mt):
#    print(name, end='\t')

#print(system())
#print(version())
#print(platform())
#print(platform(1))
#print(platform(0, 1))
#print(machine())
#print(processor())


#def plus(x, y):
#    return x + y

#def minus(x, y):
#    return x - y

#def delet(x, y):
#    return x / y

#def umnoj(x, y):
#    return x * y

#def calcul():
#    a = int(input("value 1: "))
#    b = int(input("value 2: "))
#    print(f'\nСложение: {plus(a, b)}\nВычитание: {minus(a, b)}\nДеление: {delet(a, b)}\nУмножение: {umnoj(a, b)}')


#if __name__ == "__main__":
#    calcul()

def Ups(x, y):
    if x > y: x, y = y, x
    for _ in range(x + 1, y):
       if _ % 2 == 0: print(_, end = ' ')

#def Ups():
#    print('Не сравнивайте себя ни с кем, это оскорбительно. В первую очередь для вас\nБил Гейтс')

#Ups()

Ups(int(input("value 1: ")), int(input("value 2: ")))

