#!/usr/bin/python3

import random

# Задание 1
print('\nЗАДАНИЕ 1: Пользователь вводит с клавиатуры название фрукта. Необходимо вывести на экран количество раз, сколько фрукт встречается в кортеже в качестве элемента.\n\nРЕШЕНИЕ:')
x = ('apple', 'pear', 'banana', 'orange', 'lemon', 'lime', 'grapefruit', 'pineapple', 'mango', 'peach', 'plum', 'cherry', 'strawberry', 'raspberry', 'blueberry', 'blackberry', 'grape', 'watermelon', 'melon', 'bananamango', 'strawberry-banana')
print(f'Фрукты: {x}\n')
z = input("Введите название фрукта: ")
print(f'Количество раз: {x.count(z)}')

# Задание 2
print('\n\nЗАДАНИЕ 2: Добавьте к заданию 1 подсчет количества раз, когда название фрукта является частью элемента\n\nРЕШЕНИЕ:')
i = 0
for _ in x: i += _.count(z)
print(f'Количество раз: {i}')

# Задание 3
print('\n\nЗАДАНИЕ 3: Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0 до N раз). Пользователь вводит с клавиатуры название производителя и слово для замены. Необходимо заменить в кортеже все элементы с этим названием на слово для замены. Совпадение по названию должно быть полным.\n\nРЕШЕНИЕ:')
x = ('Ford', 'Renault', 'Toyota', 'Honda', 'Hyundai', 'Kia', 'Ford', 'Lexus', 'Nissan', 'Opel', 'Peugeot', 'Volvo', 'Hyundai', 'Honda', 'Renault', 'Škoda', 'SsangYong', 'Renault', 'Toyota', 'Subaru', 'Mitsubishi', 'Toyota', 'Volkswagen', 'Volvo', 'Renault')
print(f'Производители авто: {x}\n')
a = input('Введите название производителя: ')
b = input('Введите на что нужно заменить: ')
x = tuple([b if i == a else i for i in x])
print(f'Результат: {x}')

# Задание 4
print('\n\nЗАДАНИЕ 4: Есть кортеж с целыми числами. Нужно вывести статистику по количеству цифр в элементах кортежа.\n\nРЕШЕНИЕ:')
x = tuple(random.randint(0, 999) for i in range(30))
print(f'Кортеж с целыми числами: {x}\n')
y = [0] * 3
for _ in x:
    if _ < 10: y[0] += 1
    elif _ < 100: y[1] += 1
    else: y[2] += 1
print(f'Результат:\n\tОдна цифра: {y[0]}\n\tДве цифры: {y[1]}\n\tТри цифры: {y[2]}')
