#!/usr/bin/python3

# Пораждающие патерны
# Фабрики используются для инкапсуляции информации о классах, и при этом для создания их экземпляров на основе определенных параметров, которые им предоставляются.

from abc import ABC, abstractmethod
'''
class Product(ABC):
    @abstractmethod
    def calculate_risk(self):
        pass

class Worker(Product):
    def __init__(self, name, age, hours):
        self.name = name
        self.age = age
        self.hours = hours

    def calculate_risk(self):
        return self.age + 100 / self.hours

    def __str__(self):
        return f"{self.name} [{self.age}] - {self.hours} h/week"

class Unemployed(Product):
    def __init__(self, name, age, able):
        self.name = name
        self.age = age
        self.able = able

    def calculate_risk(self):
        if self.able: return self.age + 10
        else: return self.age + 30

    def __str__(self):
        if self.able: return f"{self.name} [{self.age}] - {self.able} able to week"
        else: return f"{self.name} [{self.age}] - {self.able} - unable to week"

class PersonFactory:
    def get_person(self, type_of_person):
        if type_of_person == 'worker': return Worker("Oliver", 22, 30)
        if type_of_person == 'unemployed': return Unemployed("Sophie", 33, False)

factory = PersonFactory()
product = factory.get_person("worker")
print(product)
product2 = factory.get_person("unemployed")
print(product2)

'''
'''
Abstract Factory
Для реализации создается семейство разных предметов. Хотя они и равные, они так или иначе сгруппированы по опредлеенной характеристике.
Например, вам может понадобиться создать основное блюдо и десерт в итальянском и французском ресторане, но вы не хотите смешивать одну кухню с другой
Идея похожа на релизацию обычной фабрики, но единственное отличие состоит в том, что все фабрики имеют несколько отдельных методов для создания объектов, и тип фабрики определяет семейство объектов.
Абстрактная фабрика отвечает за создание целых групп объектов, наряду с соотвествующими фабриками, не касаясь самиъ объектов.
'''


class Product(ABC):
    @abstractmethod
    def cook(self):
        pass

class FettuccineAlfredo(Product):
    name = "Fettuccine Alfredo"

    def cook(self):
        print(f"Главное итальянское блюдо {self.name}")

class Tiramisu(Product):
    name = "Tiramisu"

    def cook(self):
        print(f"Главный итальяснский дессерт {self.name}")

class DuckALOrange(Product):
    name = "Duck A L Orange"

    def cook(self):
        print(f"Главное французское блюдо {self.name}")

class CremeBrulle(Product):
    name = "Creme Brulle"

    def cook(self):
        print(f"Главный французский дессерт {self.name}")

class Factory(ABC):
    @abstractmethod
    def get_dish(type_of_meal):
        pass

class ItallianDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "main": return FettuccineAlfredo()
        if type_of_meal == "dessert": return Tiramisu()

    def create_dessert(self):
        return Tiramisu()

class FranchDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "main": return DuckALOrange()
        if type_of_meal == "dessert": return CremeBrulle()

    def create_dessert(self):
        return CremeBrulle()

class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "italian": return ItallianDishesFactory
        if type_of_factory == "french": return FranchDishesFactory


factory = FactoryProducer()
fac = factory.get_factory("italian")
main = fac.get_dish("main")
main.cook()

dessert = fac.get_dish("dessert")
dessert.cook()

fac1 = factory.get_factory("french")
main = fac1.get_dish("main")
main.cook()

dessert1 = fac1.get_dish("dessert")
dessert1.cook()



'''
Builder
Мы создаем класс Builder, который созадет наш объект и добавляет модули нашемур роботу. Вместио замысловатого коструктора, мы можем создать экземпляр объекта и добавить необходимые компоненты с помощью функций
'''

class Robot:
    def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []

    def __str__(self):
        string = ""
        if self.bipedal: string += "BIPEDAL "
        if self.quadripedal: string += "QUADRIPEDAL "
        if self.flying: string += "FLYING ROBOT "
        if self.wheeled: string += "ROBOT ON WHEELS\n"
        else:
            string += "REBOT \n"
            if self.traversal: string += "Traversal modules installed \n"
            if self.detection_systems: string += "Detection system installed \n"
            for system in self.detection_systems: string += " - " + str(system) + "\n"
        return string

class BipedalLegs:
    def __str__(self):
        return "two legs"

class QuadripedalLegs:
    def __str__(self):
        return "four legs"

class Arms:
    def __str__(self):
        return "two arms"

class Wings:
    def __str__(self):
        return "wings"

class Blades:
    def __str__(self):
        return "Blades"

class FourWhells:
    def __str__(self):
        return "four whells"

class CameraDetectionSystem:
    def __str__(self):
        return "cameras"

class InfraredDetectionSystem:
    def __str__(self):
        return "infrared"

# Реализация паттерна

class RobotBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass

class AndroidBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.bipedal = True
        self.product.traversal.append(BipedalLegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())

builder = AndroidBuilder()
builder.build_traversal()
builder.build_detection_system()
print(builder.get_product())


'''
Prototype
Решает проблему копирования объектов путем делегирования этой задачи самим объектам. Все объекты, которые можно копировать, должны реализовывать метод clone и использовать его для получения копий объекта
'''

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class MyClass(Prototype):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        obj = MyClass(self.arg1, self.arg2)
        obj.performed_operation= self.performed_operation
        return obj
        # return deepcopy(self)

'''
Object Pool
'''


class MyClasss:
    def reset(self):
        self.setting = 0

class ObjectPool:
    def __init__(self, size):
        self.objects = [MyClasss() for _ in range(size) ]

    def acquire(self):
        if self.objects: return self.objects.pop()
        else:
            self.objects.append(MyClasss())
            return delf.objects.pop()

    def release(self, reusable):
        reusable.reset()
        self.objects.append(reusable)

pool = ObjectPool(10)
reusable = pool.acquire()
pool.release(reusable)

