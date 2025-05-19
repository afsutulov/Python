#!/usr/bin/python3

# Файл - это всего лишь набор данных, представленных в виде последовательности битов на ПК. Информация хранится в куче данных (структуре данных) и имеет название "Имя файла".
# В Python по умолчанию есть два типа данных: 1. Текстовые *.txt, *.rtf, 2. Бинарные *.bin

# Последовательность операций
# 1. Открытие файла. 2. Выполенние операции (чтение запись). 3. Закрытие потока

#f = open('test.txt', 'r')
# r - только для чтения
# w - только для записи. Если файла нет, он его создаст
# rb - только для чтения бинарного файла
# wb - только для записи бинарного файла
# r+ - для чтения и записи одновременно
# a - открытие файла для редактирования. Также создает новый файл если он не найден
# rb+, wb+, a+, ab, ab+

#print(*f) # * - распаковка любого типа данных
#f.close() # Закрытие потока

#f = open('test.txt', 'r')
#try:
#    print(*f)
#finally:
#    f.close()


#with open('test.txt', 'r') as f:
#    print(f.read(10)) # Считать 10 символов
#    print(f.readline(0))
#    print(f.readline(1))
#    print(f.readline())
#    print(*f)


#with open('practic.txt','w') as f:
#    f.write('Per aspera ad astra')

#with open('practic.txt','r') as f:
#    print(f.readlines())


#file.fileno() - проверка целостности файла
#file.flush() - очистка буфера обмена файла(потока)
#file.isatty() - возвращает True если файл закреплен дл\ работы с терминалом
#file.next() - возвращает следующую строу из файла
#file.seek() - устанавливает текущую позицию указатля в файле
#file.seekable() - проверяет доступ к файлу, слачайный доступ
#file.tell() - возвращает текущую позицию в файле
#file.truncate(n) - уменьшает размер файла. если n указано, то файл обрезается до n байт. если нет - то до текущей позиции
#file.witelbnes() - добавляет последовательность строк в файл

import os

#os.rename('test.txt', 'test123.txt') # переименовать файл

# Пример реализации приложения "Шпионаж"

def file_collector(path):
    path = os.path.normpath(path) # Нормализация пути (для windows -> linux)
    result = { "dirs":[], "files": [] }
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result['dirs'].append(dir)
        for file in filenames:
            result['files'].append(file)
    file = open('collector.txt', 'w')
    file.write('*' * 4 + f'Directories' + '*' * 4)
    for dir in result['dirs']: file.write(f'\n{dir}')
    file.write('\n\n' + '*' * 4 + f'Files' + '*' * 4)
    for fl in result['files']: file.write(f'\n{fl}')
    file.close()

path = '/home/as/SmartHome'
file_collector(path)
