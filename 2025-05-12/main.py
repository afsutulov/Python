#!/usr/bin/python3

import random

def quick_sort(mass):
    if len(mass) <= 1: return mass
    return quick_sort([x for x in mass if x < mass[len(mass) // 2]]) + [x for x in mass if x == mass[len(mass) // 2]] + quick_sort([x for x in mass if x > mass[len(mass) // 2]])

# Рекурсивная сортировка методом случайного выбора опорного элемента (piv)
def quicksort(arr):
    if len(arr) < 2: return arr
    pivot = random.choice(arr)
    return quicksort([x for x in arr if x < pivot]) + [x for x in arr if x == pivot] + quicksort([x for x in arr if x > pivot])

# Сортировка методом Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        # Выполняем сортировку вставкой для каждого подсписка с текущим размером интервала
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Перемещаем элементы подсписка в правильную позицию
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
            j -= gap
            arr[j] = temp
        gap //= 2 # Уменьшаем размер интервала
    return shell_sort


random_mass = [random.randint(-100, 100) for i in range(10)]

print(f'Массив: {random_mass}\n')
print(f'Быстрая сортировка: {quick_sort(random_mass.copy())}')
print(f'Рекурсивная сортировка методом случайного выбора опорного элемента: {quicksort(random_mass.copy())}')
print(f'Сортировка методом Шелла: {shell_sort(random_mass.copy())}')
