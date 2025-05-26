#!/usr/bin/python3

# Класс - набор объектов, методов, атрибутов, выступающий в роли контейнера (шаблона) для будущего объекта, с которым работает уже пользователь
# Объект - воплощение требований, характеристик и качеств, которые приписываются конкретному классу
class Car:
    # Конструктор класса
    def __init__(self, fuel, maxspeed):
        self.fuel = fuel
        self.maxspeed = maxspeed

    # Функция для заправки топлива
    def refuel(self, amount):
        self.fulef += amoumt

    # Функция для движения
    def drive(self):
        if self.fuel > 0:
            print(f"\tМашина едет. Топлива: {self.fuel}")
            self.fuel -= 1
        else: print("\tНет топлива")

polo = Car(50, 50)
mini = Car(10, 90)
beetle = Car(0, 110)

print("Едет polo")
for i in range(10):
    polo.drive()

print("\nЕдет mini")
for i in range(10):
    mini.drive()

print("\nЕдет beetle")
for i in range(10):
    beetle.drive()



# Написать программу "Успеваемость" студента. Пользователь вводит 10 оценок от 1 до 5. Реализовать меню для работы:
# 1. Вывод, 2. Пересдача, 3. Выходит ли ститендия? 4. Вывод отсортированных оценокпо возрастанию и убыванию

#class Student:
#    def __init__(self, spisok_ocenok):
#        self.spisok_ocenok = spisok_ocenok

#    def menu(self):
#        while True:
#            print("Меню:\n\t1. Вывод\n\t2. Пересдача\n\t3. Стипендия\n\t4. Вывод оценок по возрастнию и убыванию\n\t0. Выход")
#            print("*" * 14)
#            value = int(input("Ваш выбор: "))
#            if value == 1: self.Print()
#            elif value == 2: self.reEval()
#            elif value == 3: self.stipendia()
#            elif value == 4: self.sort_list()
#            elif value == 0: break

    # Функция вывода на экран оценок
#    def Print(self):
#        print(f"Оценки: ", end = "")
#        for i in self.spisok_ocenok: print(i, end = " ")
#        print()

    # Функция замены оценки
#    def reEval(self):
#        self.Print()
#        last_eval = int(input("Введите оценку на замену: "))
#        new_eval = int(input("Введите новую оценку: "))
#        for i in range(len(self.spisok_ocenok)):
#            if self.spisok_ocenok[i] == last_eval: self.spisok_ocenok[i] = new_eval; break
#        print("Оценка изменена!")

#    def stipendia(self):
#        if sum(self.spisok_ocenok)/len(self.spisok_ocenok) >= 4: print("Стипенция будет!")
#        else: print("Стипенции не будет!")

#    def sort_list(self):
#        if int(input("1. Убывание\n2. Возрастание\nВаш выбор: ")) == 1: self.spisok_ocenok = sorted(self.spisok_ocenok, reverse = True)
#        else: self.spisok_ocenok = sorted(self.spisok_ocenok)

#student = Student([1, 5, 3, 4, 2, 3, 5, 5, 5, 5])
#student.menu()

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self): # При обращении методом функции, которая обрабатывает строкине обходимо давать обращение конструкции встроемуо методу __str__, который вернет строку для вывода обработки
        return self.name + " in " + self.galaxy

class Vehicle: #SUPER CLASS, для ниже стоящих классов
    pass

class LandVehicle(Vehicle): # Класс-наследник - подкласс
    pass

class TrackedVehicle(LandVehicle): # Класс-наследник - подкласс
    pass


class SampleClass:
    def __init__(self, value):
        self.value = value

#class Super:
#    def __init__(self, name):
#        self.name = name
#    def __str__(self):
#        return f"Мое имя {self.name}, очень приятно!"

#class Sub(Super):
#    def __init__(self, name):
#        Super.__init__(self, name)

class Super:
    supVar = 1

class Sub(Super):
    subVar = 2


class Level1:
    varial = 100
    def __init__(self):
        self.var1 = 100
    def func1(self):
        return 102

class Level2(Level1):
    varial2 = 200
    def __init__(self):
        super().__init__()
        self.var2 = 201
    def func2(self):
        return 202

class Level3(Level2):
    varial3 = 300
    def __init__(self):
        super().__init__()
        self.var3 = 301
    def func3(self):
        return 302

class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def funB(self):
        return 22

class SuperC:
    varC = 30
    def funC(self):
        return 33

class SuperD(SuperA, SuperB, SuperC):
    pass


def main():
    sun = Star("Sun", "Milky Way")
    print(sun)

    # Наследование в ООП
    # issubclass(OneClass, TwoClass) - функция для определения отношений между классами, проверка на наследование
    for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
        for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
            print(issubclass(cls1, cls2), end= "\t")
    print()

    # isinstance(ObjName, TwoClass) - Проверка наличия у объекта определенных характеристик от класса наследника
    myVehicle = Vehicle()
    myLandVehicle = LandVehicle()
    myTrackedVehicle = TrackedVehicle()
    for obj1 in [myVehicle, myLandVehicle, myTrackedVehicle]:
        for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
            print(isinstance(obj1, cls2), end= "\t")
    print()

    # Пример 2
    obj1 = SampleClass(0)
    obj2 = SampleClass(10)
    obj3 = obj2

    obj3.value += 1
    print(obj1.value, obj2.value, obj3.value)
    # Оператор is позволяет определить относится ли две переменные, структуры или объекты к одному объекту класса
    print(obj1 is obj2)
    print(obj2 is obj3)
    print(obj3 is obj1)

    # Пример 3. Нахождение методов и атрибутов классов
#    Obj = Sub("Михаил")
#    print(Obj)

    # Пример 4.
    obj = Sub()
    print(obj.subVar)
    print(obj.supVar)

    # Пример 5
    obj = Level3()
    print(obj.varial, obj.var1, obj.func1())
    print(obj.varial2, obj.var2, obj.func2())
    print(obj.varial3, obj.var3, obj.func3())

    # Пример 6. Множественное наследование
    obj = SuperD()
    print(obj.varA, obj.varB, obj.varC)
    print(obj.funA(), obj.funB(), obj.funC())

if __name__ == "__main__": main()
