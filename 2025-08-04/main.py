#!/usr/bin/python3

'''
Паттерн Adapter
Необходим для решения проблем:
1. Клиент должен сделать запрос к приложению через адаптер, вызвав на нем метон с помощью целового интерфейса.
2. Используя интерфейс адаптационного клиента, адаптер должен перевести этот запрос на пользователя.
3. Результат звонка принимается клиентом и он не подозревает о присутствии адаптера


Пример:
'''

class MotoCycle:
    def __init__(self):
        self.name = "MotoCycle"

    def TwoWheller(self):
        return "TwoWheller"

class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheller(self):
        return "EightWheller"

class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheller(self):
        return "FourWheller"

#Класс Адаптер для транспорта
class Adapter:
    def __init__(self, obj, **adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__

if __name__ == "__main__":
    objects = []
    motoCycle = MotoCycle()
    objects.append(Adapter(motoCycle, wheels=motoCycle.TwoWheller()))
    truck = Truck()
    objects.append(Adapter(truck, wheels=truck.EightWheller()))
    car = Car()
    objects.append(Adapter(car, wheels=car.FourWheller()))
    for obj in objects:
        print(f"{obj.name} --- {obj.wheels}")
'''
Преимущества:
1. Принцип единной ответственности: можно отделить код от первичной логики клиента
2. Гибкость: возможность повторного использования кода
3. Менее сложный класс (декомпозиция): такие классы могут быть реализованы методами полиморфизма и наследования
4. Принцип Open/Close: мы можем вводить в код другие классы, не ломая логику работы программы адаптера

Недостатки:
1. Сложность кода: чем больше классов, тем сложнее классы взаиодействуют друг с другом
2. Отношение к наследованию: когда мы хотим повторно использовать код, т.е. класы и интерфейсы, к которым не зхватает функций, это можно сделать с помощью методов адаптера.
'''


'''
Паттерн Мост(Bridge)
Позволяет отделять абстракции, специфичные для реализации и абстракции, независимые от реализации, друг от друга, создавая отдельные сущности для классов.
Элементы создания моста:
1. Абстрауция - ядро шаблона, которое обеспечивает ссылку на реализацтора
2. Расширение - улучшение абстракции, поднятие мелких деталей (параметров и методов) н аодин уровень выше и скрывает более мелкие элементы от исполнителей
3. Определение - создание инерфейса для классов реализации
4. ТЗ - выполнение всех параметров и указаний исполнителя

Создадаим класс Cuboid с тремя параметрами: lenght, broadth, height
И тремя методами на реализацию: produceWithAPIOne(), produceWithAPITwo(), expand()
Основная задача: отделить абстрацию, зависящую от конкретной реализации
'''
class ProducingAPI1:
    def produceCuboid(self, lenght, breadth, height):
        print(f"API1 is producing Cuboid with lenght = {lenght}, breadth = {breadth}, height = {height}")

class ProducingAPI2:
    def produceCuboid(self, lenght, breadth, height):
        print(f"API2 is producing Cuboid with lenght = {lenght}, breadth = {breadth}, height = {height}")

class Cuboid:
    def __init__(self, lenght, breadth, height, producingAPI):
        self._lenght = lenght
        self._breadth = breadth
        self._height = height
        self._producingAPI = producingAPI

    def produce(self):
        self._producingAPI.produceCuboid(self._lenght, self._breadth, self._height)

    def expand(self, times):
        self._lenght = self._lenght * times
        self._breadth = self._breadth * times
        self._height = self._height * times

print()
cuboid1 = Cuboid(1, 2, 3, ProducingAPI1())
cuboid1.produce()
cuboid2 = Cuboid(4, 5, 6, ProducingAPI2())
cuboid2.produce()
cuboid2.expand(2)
cuboid2.produce()


'''
Составной метод(Composite)
Описывает группы объектов, которые обрабатываются также, как и отдельный экземпляр объекта общего типа.
Основная цель - обработать сложные структуры древовидной формы и скомпоновать контейнер из объектов

Пример:
Обработка методов расчета общей запрплта сотрудников.
'''

class LeafElement:
    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print(self.position)

class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def rempve(self, child):
        self.children.pop(child) #remove()

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t ", end = ' ')
            child.showDetails()

topLevelMenu = CompositeElement("GeneralManager")
subMenuItem1 = CompositeElement("Namager1")
subMenuItem2 = CompositeElement("Namager2")
subMenuItem11 = LeafElement("Developer11")
subMenuItem12 = LeafElement("Developer12")
subMenuItem21 = LeafElement("Developer21")
subMenuItem22 = LeafElement("Developer22")
subMenuItem1.add(subMenuItem11)
subMenuItem2.add(subMenuItem21)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.showDetails()


'''
Декоратор(Decorator)
Позволяет приклреплять поведения к объектам, не изменяя их структуру и реализацию, помещая объекты внутрь оболочки, содержащих поведение
'''

class WrittenText:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class UnderliteWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def __str__(self):
        return f"<u>{self._wrapped}</u>"

class ItalicWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def __str__(self):
        return f"<i>{self._wrapped}</i>"

class BoldWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def __str__(self):
        return f"<b>{self._wrapped}</b>"

before_gfg = WrittenText("ACADEMY TOP")
after_gfg = ItalicWrapper(UnderliteWrapper(BoldWrapper(before_gfg)))

print(f"before: {before_gfg}")
print(f"after: {after_gfg}")


'''
Метод Flywight
Направлен на минимизацию количества объектов, необходимых программе во время ее выполнения. По сути, он создает объект, который является общим для нескольких контекстов. Он создан таким образом, что вы не можете отличить объект от объекта.
Главная особенность - налетный вес объектов - они неизменяемы.
'''
class ComplexCars(object):
    def __init__(self):
        pass

    def cars(self, car_name):
        return f"ComplexPattern {car_name}"

class CarFamilies(object):
    car_family = {}

    def __new__(cls, name, car_family_id):
        try:
            id = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
        cls.car_family[car_family_id] = id
        return id

    def set_car_info(self, car_info):
        cg = ComplexCars()
        self.car_info = cg.cars(car_info)

    def get_car_info(self):
        return self.car_info

car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferarri'), ('b', 1, 'Audi'))
car_family_objects = []

for i in car_data:
    obj = CarFamilies(i[0], i[1])
    obj.set_car_info(i[2])
    car_family_objects.append(obj)

for i in car_family_objects:
    print(f"id = {id(i)}")
    print(i.get_car_info())
