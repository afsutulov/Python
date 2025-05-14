#!/usr/bin/python3

# Кортеж - неизменяемая структура данных, которая по своему подобию похожа на список

#a = [1, 2, 3]
#a[1] = 5
#print(a)

#b = (1, 2, 3)
#b[1] = 15 - ошибка TypeError
#print(b)
# Плюсы: 1. Экономия места в памяти 2. В процессе работы в безопасности 3. Меньше ресурсов, больше производительность

#print(type(b)) # class typle
#print(b[1])
#del b

lst = [1,2,3,4,5]
print(type(lst))
print(lst)
tpl = tuple(lst)
print(type(tpl))
print(lst)

# Словари (dict) - неупорядоченная структура данных, которая позволяет хранить в себе данные в формате пар ключ:значение

dic = {"Персона": "Человек", "Марафон": "Гонка бегунов длинной около 26 миль", "Айфон": "15"}
print(dic["Персона"])

dic2 ={(1,2.2,0.2):"Кортежи могут бытьключами", 1: "Целые числа могут быть ключами", "БЕЖАТЬ":"строки тоже" }
print(dic2[(1,2.2,0.2)])

dic3 = {True: 'yes', 1: 'no', 1.0: 'maybe'}
print(dic3[True])

# Работа со словарями

d = {}
d = {'dict_key': 'dict_value'}
d = dict(short='dict', long='dictionary')
d['index'] = 20
d = dict.fromkeys(['a', 'b'], 100)
print(d)

key_list = ['marvel', 'dic']
value_list = ['Spideman', 'Batman']
super = dict(zip(key_list, value_list))
print(super)

d = {i: i ** 2 for i in range(10)}
print(d)

# Получение данных из словаря

dic4 = {'Марафон': 26}
print(dic4['Марафон'])  #Получим ошибку если ключа не будет существовать"
# Для лучшего использвоания лучше использовать метод *.get()
# Для удаления данных используется метод del
# d.clear() отчищает словарь от всех пар, но не удаляет переменную
# d.copy() копирует данные

d = dic4

print(id(d))
print(id(dic4))
print(dic4.get('Марафон'))

#dic = {"Персона": "Человек", "Марафон": "Гонка бегунов длинной около 26 миль", "Айфон": "15"}
#dic.update('Марафон': '33км')
#print(dic)

#dic.pop(key) - удаляет ключ и удаляет его значение
#dic.setdefault('name') - изет ключ и возвращает его значение, если он ен найден - создает этот ключ со значение None
#d.case() - возвращает список ключей в словаре
#d.values() - возвращает список значений ключей
#d.items() возвращает пары ключ: значение
print(d.items())

# Примеры
# Интеграция через консоль

story = {'Сто': 100, 'Двести': 200, 'Тристо': 300}

for key in story:
    print(key)

for key in story.values():
    print(key)

for key in story.items():
    print(key)


# Сортировка словаря

people = {3: 'jim', 4: 'oga', 1: 'max', 5: 'ivan', 6: 'kirill' }
print(sorted(people.values()))
p = list(people.values())
print(p[1])

# Если задача состоит в том, что словарь слишком большой, а вам нужна лишь его часть - вам поможет метод islice()

import itertools

nd = dict(itertools.islice(people.items(), 0, 3 ))
print(nd)

people = {}
for key, value in people.items():
    temp = [key, value]
    people.append(temp)

print(people)


#Множества (set) - контейнер, содержащий не повторяющиеся элементы в случайном порядке

s = set()
print(type(s))
s = set('Hello')

s = {i ** 2 for i in range(10)}
print(s)


#Методы
#len
#x in s -  проверка принадлежности
#s.isdisjount(other) - истина, если set и other не имеет общих элементов
#set == other - проверка всех элементов множества на пересечение с другим множеством
#s.issubset(other) - проверка принадлежности множества
#s.issuperset(other) - проверка второго множества на вхождение в первое
#s.union(other, ...) - объединение нескольких множеств
#s.intersection(other) - пересечение множеств
#s.difference() - множество элементов уникальных в 2х множествах
#s.symmetric_difference() - уникальные встречающиеся элементы
#s.copy() - копировние

product = {'Apple', 'Tesla', 'DNS'}
company1 = {'Samsung', 'Sony'}
company2 = {'Apple', 'BMW', 'IBM'}
company3 = {'BMW', 'Tesla', 'DNS', 'Ferrary'}

print()

# Совпадения
print(product.intersection(company1))
print(product.intersection(company2))
print(product.intersection(company3))
print()

# Акции которых нет у нас
print(product.difference(company1))
print(product.difference(company2))
print(product.difference(company3))
print()
# Разница в товарах
print(product.symmetric_difference(company1))
print(product.symmetric_difference(company2))
print(product.symmetric_difference(company3))
print()

# Журнал Юзера

my_dict =   {'Nikita': {'tel': '1234567', 'OK': 'ok.ru/nikita', 'vk': 'vk.com/nikita', 'nic': 'dolbaeb'},
            'Marina': {'tel': '4545453', 'OK': 'ok.ru/marina', 'vk': 'vk.com/marina', 'nic': 'celka'},
            'Max': {'tel': '6543434', 'OK': 'ok.ru/max', 'vk': 'vk.com/max', 'nic': 'duren'},
            }

user = input('Введите имя пользователя: ')

print(my_dict[user]['tel'])
