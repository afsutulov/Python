#!/usr/bin/python3

import random

# 1 Пузырьковая сортировка
def bubble_sort(mass):
    for i in range(len(mass)):
       for j in range(i, len(mass)):
          if mass[i] > mass[j]: mass[i], mass[j] = mass[j], mass[i]
    return mass

# 2 Сортировка выборкой - делит список на две части: отсортированный и неотсортированный
def selection_sort(mass):
    for i in range(len(mass)):
       lowest = i
       for j in range (i+1, len(mass)):
          if mass[j] < mass[lowest]: lowest = j
       mass[i], mass[lowest] = mass[lowest], mass[i]
    return mass

# 3 Сортировка вставками
def insert_sort(mass):
    for i in range(1, len(mass)): # Начинаем сортировку со второго элемента т.к. считаем, что 1 элемент уже отсортирован
       item = mass[i] # Элемента для вставки
       j = i - 1 # Сохраняем ссылу на индекс предыдущего элемента
       while j >= 0 and mass[j] > item:
          mass[j + 1] = mass[j]
          j -= 1
          mass[j + 1] = item
    return mass

# 4 Пиромидальная сортировка (ебейшее говно!)
def heapify(mass, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and mass[i] < mass[l]:
        largest = l
    if r < n and mass[largest] < mass[r]:
        largest = r
    if largest != i:
        mass[i], mass[largest] = mass[largest], mass[i]
        heapify(mass, n, largest)

def heap_sort(mass):
    n = len(mass)
    for i in range(n, -1, -1):
        heapify(mass, n, i)
    for i in range(n - 1, 0, -1):
        mass[i], mass[0] = mass[0], mass[i]
        heapify(mass, i, 0)
    return mass

# 6 Быстрая сортировка
def quick_sort(mass):
    if len(mass) <= 1: return mass
    pivot = mass[len(mass) // 2]
    left = [x for x in mass if x < pivot]
    middle = [x for x in mass if x == pivot]
    right = [x for x in mass if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

random_mass = [random.randint(-100, 100) for i in range(10)]

print(f'Массив: {random_mass}\n')
print(f'Пузырьковая сортировка: {bubble_sort(random_mass.copy())}')
print(f'Сортировка выборкой: {selection_sort(random_mass.copy())}')
print(f'Сортировка вставками: {insert_sort(random_mass.copy())}')
print(f'Пиромидальная сортировка: {heap_sort(random_mass.copy())}')
print(f'Быстрая сортировка: {quick_sort(random_mass.copy())}')

random_mass.sort()
print(f'Сортировка встроенной функцией: {random_mass}')
