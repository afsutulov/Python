#!/usr/bin/python3

# Инкапсуляция - это второй принцип ООП, благодаря которому классы могут скрывать внутренние элементы (атрибуты функции) от внешнего мира
# Реализуется с помощью методов и атрибутов Private and Protected.
# Private - обозначается с помощью двойного подчеркивания "__" перед именем.
# Доступны только внутри класса. Из вне к ним обратиться нельзя. 
# Protected -  обозначается с помощью одиночного подчеркивания "_" перед именем.
# Условно защищены, но Python не запрещает доступ ним.

#class BankAccount:
#    def __init__(self, owner, balance):
#        self._owner = owner # Защищенный атрибут
#        self.__balance = balance # Приватный атрибут

#    def deposit(self, amount):
#        if amount > 0: self.__balance += amount; print(f"Депозит {amount} успешно выполнен")
#        else: print("Сумма доллжна быть положительной.")

#    def widha(self, amount):
#        if 0 < amount  < self.__balance: self.__balance -= amount; print(f"Снятие {amount} успешно")
#        else: print("Недостаточно средств")

#    def get_balance(self):
#        return self.__balance

#    def set_balance(self, amount):
#        self.__balance = amount

#account = BankAccount("Иван Иванов", 1000)
#print(f"Имя вкладчика: {account._owner}")
#print(account.get_balance())
#account.set_balance(2000)
#print(account.get_balance())
#account.widha(200)
#print(account.get_balance())

# Полиморфизм - 3 столп ООП, заключается в итпользовании единственной сущности (метода, оператора, объета) для обработки различных типов в разлисных сценариях.

# Пример 1.
#num1 = 1
#num2 = 2
#print(num1 + num2)

#str1 = "Python"
#str2 = "3.13"
#print(str1 + str2)

# Пример 2. Полиморфизм функций
#print(len("PROGRAMMING"))
#print(len(["A", "B", "C"]))
#print(len({"Name": "IVAN", "AGE": 56, "ADDRESS": "PERM"}))

# Пример 3. Полиморфизм в классах
#class Animal:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def info(self):
#        print(f"Привет, я животное. Меня зовут {self.name}. Мне {self.age} лет")

#    def make_sound(self):
#        print("Делаю звуки животного.")


#class Cat(Animal):
#    def __init__(self, name, age):
#        Animal.__init__(self, name, age)

#    def info(self):
#        print(f"Привет, я кошка. Меня зовут {self.name}. Мне {self.age} лет")

#    def make_sound(self):
#        print("Мяууу")

#class Dog(Animal):
#    def __init__(self, name, age):
#        Animal.__init__(self, name, age)

#    def info(self):
#        print(f"Привет, я собака. Меня зовут {self.name}. Мне {self.age} лет")

#    def make_sound(self):
#        print("Гав-Гав")

#dog = Dog("Шарик", 10)
#cat = Cat("Мурка", 6)

#for animals in (dog, cat):
#    animals.make_sound()
#    animals.info()
#    animals.make_sound()


# Пример 4. Переопределение методов

#from math import pi

#class Shape:
#    def __inti__(self, name):
#        self.name = name

#    def area(self):
#        pass

#    def fact(self):
#        return "Я фигура для подсчета."

#    def __str__(self):
#        return self.name

#class Square(Shape):
#    def __init__(self, length):
#        self.length = length
#        Shape.__init__("Square")

#    def area(self):
#        return self.length**2

#    def fact(self):
#        return "У меня все углы 90 градусов."

#class Circle(Shape):
#    def __init__(self, radius):
#        self.radius = radius
#        Shape.__init__("Circle")

#    def area(self):
#        return pi * self.radius ** 2



#a = Square(4)
#b = Circle(5)

#print(b.fact())
#print(a.fact())
#print(b.area())
#print(b)
#print(a)

class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        if "Николай" in self.name: return self.name
        else: return f"Я не {self.name}, а Николай"

print(Nikola("Николай Петрович", 40))
print(Nikola("Владлен", 30))


# Перегрузка (переопределение) мотодов в классе

# Сложение a + b  __add__(a, b)
# Объединение seq1 + seq2 __concat__(seq1, seq2)
# Проверка наличия obj in seq __constains__(seq, obj)
# Деление a / b __ttuediv(a, b)
# Поразрядное И a & b __add__(a, b)
# Поразрядное ИЛИ a ^ b __xor__(a, b)
# Поразрядное инверсия ~a __invert__(a)
# Поразрядное И ИЛИ a | b  __or__(a, b)
# Степень  a ** b __pow__(a, b)
# Присвоение по индексу obj[k] = a __setitem__(obj, k, a)
# Удаление по индексу del obj[k]  __delitem__(obj, k)
# Обращение по индексу obj[k] __getitem__(obj, k)
# Остаток от деления a % b __mod__(a, b)

# Пример 6
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных методов: 1. Проверка н аравенство радиусов двух окружностей (==)
# 2. Сравнение длин двух окружностей (<, >, <=, >=)
# 3. Пропорциональное изменение раземров окружносетй, путем изменения радиуса (+, -, +=, -=)

import math

class Circle:
    def __init__(self, radius):
        if radius <= 0: raise ValueError("Радиус должен быть положительный")
        self.radius = radius

    def circleference(self): # Длинна окружности
        return 2 * math.pi * self.radius

    def __eq__(self, other): # Сравнение объектов по длинне
        if not isinstance(other, Circle): return NotImpplement
        return self.radius == other.radius

    def __gt__(self, other):
        return self.circleference() > other.circleference()

    def __le__(self, other):
        return self.circleference() <= other.circleference()

    def __ge__(self, other):
        return self.circleference() >= other.circleference()

    def __add__(self, other): # Сумма
        return Circle(self.radius + other.radius)

    def __str__(self):
        return f"Circle radius = {self.radius}"

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__( self, value):
        self.radius -= value
        return self

circle1 = Circle(5)
circle2 = Circle(7)

print(circle1 == circle2)
print(circle1 > circle2)
print(circle1 >= circle2)
circle3 = circle1 + circle2
print(circle3)

circle1 += 3
circle2 -= 1

print(circle1)
print(circle2)
circle4 = circle1 - circle2
print(circle4)
