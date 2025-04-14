# if (условие):
	# действие
# elif (условие):
	# действие
# elif...
# else:
	# действие

#value = int(input("Введите число: "))

#if value > 0:
#	print("Число положительное!")
#elif value < 0:
#	print("Число отрицательное!")
#else:
#	print("Число равно нулю!")

# value1 == value2
# value1 != value2
# value1 > 0
# value1 < 0
# value >= 0
# value <= 0

#age = int(input("Введите ваш возраст: "))

#if age < 10 and age > 0:
#	print('Вы еще малыш')
#elif age >= 10 and age < 21:
#	print('Вы подросток')
#elif age >= 21 and age < 45:
#	print('Вы молодой')
#elif age >= 45 and age < 100:
#	print('Вы пенсионер')
#else:
#	print('Некорректное значение')


#time = int(input('Введите значение текущего времент в часаъ: ')) % 24
#ticket = False
#money = True
#luggage = False
#print(money or ticlet and not luggage and time > 6)

#car_speed = 50
#if (car_speed >= 50 or car_speed <= 120) and car_speed != 200:
#	print('Машина двигается быстро. Снизьте скорость!')

# Исключения. Обработка событий ошибки

#try:
#	amount = int(input('Введите число предметов: '))

#except ValueError:
#	print('Ошибка! Введите только число!!!')

#value = int(input('Введите число 1: '))
#value2 = int(input('Введите число 2: '))

#try:
#	print(f'Деление: {value / value2}')

#except ZeroDevisionError:
#	print('Делить на 0 нельзя!')

#finally:
#	print('Вействие с делением было выполено')


def Num(a):
    Flag = True
    while Flag:
        value = input(f'{a}: ')
        if value.isdigit():
           Flag = False
           return int(value)
        else:
           print('\nОшибка! Ввведено не число!')


# Четность 2
#value = Num('Введите число')

#if value % 2 == 0:
#	print('even')
#else:
#	print('odd')


# Четность 7
#value = Num('Введите число')

#if value % 7 == 0:
#	print('Number is multiple 7')
#else:
#	print('Nubmer is not multiple 7')


#value = Num('Введите чило 1')
#value2 = Num('Введите чило 2')

#if value > value2:
#   print(value)
#else:
#   print(value2)


#value = Num('Введите чило 1')
#value2 = Num('Введите чило 2')

#if value < value2:
#   print(value)
#else:
#   print(value2)


# Выбор действия с двумя числами
value = Num('Введите чило 1')
value2 = Num('Введите чило 2')

print('Какое действие совершить:\n\t1 - сложение\n\t2 - разность\n\t3 - умножение\n\t4 - деление')
x = Num('Введите цифру')

match x:
    case 1: print(f'\nРезультат: {value + value2}')
    case 2: print(f'\nРезультат: {value - value2}')
    case 3: print(f'\nРезультат: {value * value2}')
    case 4: print(f'\nРезультат: {value / value2}')
    case _: print('Введена некорректная цифра')

#if x == 1:
#    print(f'\nРезультат: {value + value2}')
#elif x == 2:
#    print(f'\nРезультат: {value - value2}')
#elif x == 3:
#    print(f'\nРезультат: {value * value2}')
#elif x == 4 and value2 != 0:
#    print(f'\nРезультат: {value / value2}')
#else:
#    print('Введена некорректная цифра')

