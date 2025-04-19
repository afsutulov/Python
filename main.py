# print('Hello world!!!\n')
# Функция для печати текста и его вывода в консоль

#name = input('Введите ваш имя: ')
#age = input('Введите ваш возраст: ')

#print(f'Привет, {name}! Тебе, {age} лет')

# Калькулятор

#value1 = int(input("Введите первую переменную: "))
#value2 = int(input("Введите вторую переменную: "))

#print(f'\nСумма: {value1 + value2}')
#print(f'Вычитание: {value1 - value2}')
#print(f'Умножение: {value1 * value2}')
#print(f'Деление целое: {value1 / value2}')
#print(f'Деление целая часть: {value1 // value2}')
#print(f'Деление остаток: {value1 % value2}')
#print(f'Возведение в степень: {value1 ** value2}')
#print("*" * 11) # одинадцать звездочек

# Проверка и сравнение данных

#print(f'Первое значение больше второго: {value1 > value2}')
#print(f'Первое значение меньше второго: {value1 < value2}')
#print(f'Первое значение рано второму: {value1 == value2}')
#print(f'Первое значение не рано второму: {value1 != value2}')
#print(f'Первое значение равно "Hello World": {value1 == 'Hello World'}')

#value_number = int(input("Введите зарплату: "))
#value_number2 = int(input("Введите платеж по кредиту: "))
#value_number3 = int(input("Введите коммуналку: "))

#result = value_number - value_number2 - value_number3

#print(f'\nЗарплата: {value_number}\n'
#	f'Платеж по кредиту: {value_number2}\n'
#	f'Платеж по коммукалке: {value_number3}\n'
#	f'Сухой остаток: {result}')

# Экранирование символов
# Вызов спец символа \ для создания команды вставки символа
# \\ - добавляет обратный слэш
# \' - добавляет кавычки
# \" - добавляет двойные кавычки
# \n - переход на новую строку
# \t - добавляет табуляцию (три пробела)
# \b - удаление предыдущего символа

#string = 'Фраза для работы со строкой'

#print(value_number, string, value_number2, value_number3, sep='*\n')

# sep - строка для вставки между значениями элементов вывода для print
# end - вставка символа в конце строки, вместо \n

#print(value_number, string, value_number2, value_number3, end='***')

#print('\nto be\n\tor_not\n\t\tto_be')

#v1 = input('Введите число 1: ')
#v2 = input('Введите число 2: ')
#v3 = input('Введите число 3: ')

#print(f'Результат: {v1+v2+v3}')

val = input('Введите цифру: ')
result = 1
if val.isdigit():
	for _ in val:
		result = result * int(_)
	print(f'Произведение составых цифр: {result}')


# Строки и их свойства
string = 'my Name is AaA'
print(type(string)) # проверка типа данных
print(string + string) # сложение строк
print(string * 4) # умнжение строк
print(string.capitalize()) # Приводит первую букву в верхний регистр
print(string.lower()) # Все буквы в нижнем регистре
print(string.swapcase()) # меняет текущий регистр на противоположный
print(string.title()) # Преобразует первые буквы всех слов в верхний регистр
print(string.upper()) # Все буквы в верхнем регистре
print(string.count('my', 0, 5)) # Подсчитывает количество элементов в строке
print(string.startswith('aA')) # Проверяет начинается ли строка подстрокой
print(string.endswith('aA')) # Проверяет заканчивается ли строка подстрокой
print(string.find('is')) # Ищет подстроку в строке (слева на право). Возвращает индекс первого вхождения
print(string.rfind('AaA')) # Ищет подстроку в строке (справа на лево). Возвращает индекс первого вхождения
print(string.index('is')) # тоже что и find. Если элемента нет - будет ошибка
print(string.rindex('AaA')) # тоже что и rfind. Если элемента нет - будет ошибка

# классификация определения строк
print(string.isalnum()) # определяет, состоит ли строка из букв и чисел
print(string.isalpha()) # определяет, состоит ли строка из букв
print(string.isdigit()) # определяет, состоит ли строка из чисел
print(string.islower()) # определяет, все ли буквы в нижнем регистре
print(string.isupper()) # определяет, все ли буквы в верхнем регистре
print(string.istitle()) # определяет, первые буквы всех слов в верхний регистр
print(string.isspace()) # проверяет наличие в строке пробелов

# форматирование и выравнивание строк

print('main'.center(10, '*')) # выравнивание по цетнтпру
print('main\tmain'.expandtabs(10)) # заменяет табуляцию на количество пробелоа
print('main main'.ljust(12, '@')) # выравнивание по левому краю
print('main main'.rjust(12, '?')) # выравнивание по правому краю
print('  main main  '.lstrip()) # вырезать все пробельные символы с левого края
print('  main main  '.rstrip()) # вырезать все пробельные символы с правого края
print('  main main  '.strip()) # вырезать все пробельные символы в лева и справа
print('  main main  '.replace(' ', '=')) # заменяем подстроку

# string - тип данных для текста
# int - тип данных для целого числа
# float - тип данных числа с плавающей точкой
# bool - тип данных логический True / False
