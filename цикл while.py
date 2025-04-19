
# цикл while

# while (условие):
    # программа

#while True:
#   try:
#       age = int(input('Введите свой возраст: '))
#   except ValueError:
#       print('Введите корректное значение')
#       continue # завершает текущую итерацию, игнорирует внутренний код и начинает новый виток цикла
#   break # используется как точка выхода из цикла

#print(f'Вы ввели свой возраст {age}, вы старый')

#i = 0

#while i <= 10:
#   print(i**2)
#   i += 1

#f = 1
#valueuser = int(input('Введите значение для факториала: '))
#i = 1

#while i <= valueuser:
#    f *= i
#    print(f'Шаг {i}, значение факториала: {f}')
#    i += 1

#print(f'Ваш факториал равен: {f}')

# Проверка строки на полиндром через цикл while

#stringuser = input('Введите строку для проверки: ')
#x = ''

#i = 0
#while i < len(stringuser):
#   x = stringuser[i] + x
#   i += 1

#for _ in stringuser:
#   x = _ + x

#if stringuser == stringuser[::-1]:
	#if stringuser == ''.join(reversed(stringuser)):
#  print('Истина')
#else:
#  print('Ложь')


# Мето среза строки
# stringA = 'Hello world'
# a = stringA[6] # 'w'
# b = stringA[0:5] # 'Hello'
# c = stringA[0:5:-1] # 'olleH'
# d = stringA[0:5:2] # 'Hlo'
# stringB = ''.join(reversed(stringA)) # 'dlrow olleH'
# stringC = ','.join(reversed(stringA)) # 'd,l,r,o,w, ,o,l,l,e,H'
# stringD = ' '.split(stringA) # 'Helloworld'

