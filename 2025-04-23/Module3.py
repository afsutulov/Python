#!/usr/bin/python3

# Создание и объявление списков
category = ['Drama', 'Comedy', 'Fantasy']
ls = []
var1 = var2 = var3 = 0
ls2 = list((var1, var2, var3))

# Вывод данных из списка
print(category)

for i in category:
    print(i)

for i in range(len(category)):
    print(category[i])

# Функции списка
ls3 = []
ls3.append(2) # Функция добавлет новый элемент в конец списка
print(ls3)

ls3.pop() # Функция для удаления элемента. Если указать индекс - будет удален элемент по индексу. Если не указано - удаляется последний элемент
#ls3.remove() # Удаление первого вхождения элемента
#ls3.clear() Удаляет все элементы из списка

print(category.index('Comedy')) # Определение индекса элемента в списке

category.append('Comedy')
print(category.count('Comedy')) # Считает все вхождения элементов в список

category.sort() # Выполняет сортировку элементов
print(category)

category.reverse() # Выполняет переворот списка
print(category)

# Заполнение списков
import random

mylist = []
for i in range(10):
    mylist.append(random.randint(1, 50))
print(mylist)

mylist2 = [i for i in range(10)] # Генератор рсписков [значение + условие]
print(mylist2)

mylist3 = [i + '_' for i in 'abcdefg']
print(mylist3)

mylist4 = [i*i for i in range(1, 11) if i % 2 == 0]
print(mylist4)

customers = ['bob', 'anna', 'anton', 'max', 'nick', 'bob', 'joe']
customers2 = [i for i in customers if i != 'bob' and i != 'joe']
print(customers2)

mylist5 = [x * y for x in range(10) for y in range(10)]
print(mylist5)

mylist6 = [[x * y for x in range(10)] for y in range(1, 4)]
print(mylist6)

# Особенности списков, ссылки и клонирование

# Псевдоним - это переменные, которые имеют разные имена, но содержат одинаковые адреса памяти
# Данная особенность важна, т.к. можно случайно работая с одной переменной, испортить значение хранящиеся в другой

list1 = [1,2,3,4,5]
print(list1)
#list2 = list1
list2 = list1.copy() # Копирование списка и присвоение ему нового контейнера
list2 = list(list1) # тоже самое, что и выше
print(list2)
list2[1] = 'Hello'
print(list2)
print(list1)

# Матрицы
# Нужны для хранение данных, представленных в виде пространств или таблиц

myTb1 = [[111, 112, 113], [221, 222, 223]]

for i in range(len(myTb1)):
    for j in range(len(myTb1[0])):
        print(myTb1[i][j])

# max(), sum(), min() - минимальное значеине в списке, сумма списка и максимальное значение в списке
print(mylist3[1:6])

# Пользоваотель водит с клавиатуры эдементы списка целых и некоторое число
# Посчиитать количество вхождений этого числа
# Необходимо посчитать сумму всех четных элементов списка, среднее арифметическое всех нечетных элементов списка. Результаты вывести на экран

mylist = []
count_value = int(input('Введите числов для подсчета: '))
while True:
    value = int(input('Введите число для списка (0 выход)'))
    if value == 0: break
    mylist.append(value)

print(f'Количество элементов: {mylist.count(count_value)}')
print(f'Сумма четных элементов: {sum([i for i in mylist if i % 2 == 0])}')

_ = [i for i in mylist if i % 2 != 0]
print(f'Среднее арифметическое нечетныйх чисел: {sum(_) / len(_)}')

