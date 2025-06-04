#!/usr/bin/python3

# Классы Задания 1
class Device:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.device = "Устройство"

    def __str__(self):
        return f"{self.device} {self.name} установлен(а) по адресу: {self.address}"

    def On(self):
        return f"\n{self.device} {self.name} по адресу {self.address} включен(а)"

    def Off(self):
        return f"\n{self.device} {self.name} по адресу {self.address} выключен(а)"


class CoffeeMachine(Device):
    def __init__(self, name, address):
        Device.__init__(self, name, address)
        self.device = "Кофемашина"

    def Varit(self):
        return f"\n{self.device} {self.name} по адресу {self.address} варит кофе"

class Blender(Device):
    def __init__(self, name, address):
        Device.__init__(self, name, address)
        self.device = "Блендер"

    def Vzbivaet(self):
        return f"\n{self.device} {self.name} по адресу {self.address} взбивает продукты"

class MeatGrinder(Device):
    def __init__(self, name, address):
        Device.__init__(self, name, address)
        self.device = "Мясорубка"

    def Rubit(self):
        return f"\n{self.device} {self.name} по адресу {self.address} рубит мясо"

# Классы Задания 2
class Ship:
    def __init__(self, name, tip, volume):
        self.name = name
        self.tip = tip
        self.volume = volume
        self.model = "корабль"

    def __str__(self):
        return f"\n{self.tip} {self.model} \"{self.name}\" водоизмещением {self.volume} тонн"

    def On(self):
        return f"\n{self.tip} {self.model} \"{self.name}\" водоизмещением {self.volume} тонн поплыл"

    def Off(self):
        return f"\n{self.tip} {self.model} \"{self.name}\" водоизмещением {self.volume} тонн приплыл"

    def Dead(self):
        return f"\n{self.tip} {self.model} \"{self.name}\" водоизмещением {self.volume} тонн подбит и утонул"

class Frigate(Ship):
    def __init__(self, name, tip, volume):
        Ship.__init__(self, name, tip, volume)
        self.model = "фригат"

    def Storoj(self):
        return f"\n{self.tip} {self.model} \"{self.name}\" водоизмещением {self.volume} заступил на дежурство и сторожит"

class Destroyer(Ship):
    def __init__(self, name, tip, volume):
        Ship.__init__(self, name, tip, volume)
        self.model = "эсминец"

    def Ebosh(self):
        return f"\n{self.tip} {self.model} \"{self.name}\" водоизмещением {self.volume} проводит борьбу с подводными лодками"

class Cruiser(Ship):
    def __init__(self, name, tip, volume):
        Ship.__init__(self, name, tip, volume)
        self.model = "крейсер"

    def Ogon(self):
        return f"\n{self.tip} {self.model} \"{self.name}\" водоизмещением {self.volume} проводит огневую поддержку сухопутных войск"

# Классы Задания 3
class Money:
    def __init__(self, rub=0, kop=0):
        self.rub = rub
        self.kop = kop

    def __str__(self):
        return f"Денег: {self.rub}.{self.kop}р"

    def Num(self, txt):
        self.txt = txt
        _ = input(f'{self.txt}: ')
        if _.isnumeric(): return int(_)
        else: print(f'Ошибка ввода! Необходимо ввести число!\n'); return self.Num(txt)

    def addRub(self):
        self.rub = self.Num("Введите количество рублей")

    def addKop(self):
        self.kop = self.Num("Введите количество копеек")
        while self.kop > 100:
            self.kop -= 100
            self.rub += 1

def main():
    print("ЗАДАНИЕ 1:")
    coffee = CoffeeMachine("BOSH", "г. Пермь, ул. Лениа 1")
    print(coffee, coffee.On(), coffee.Off(), coffee.Varit())
    blender = Blender("Electrolux", "г. Березники, ул. Шахтеров 33")
    print(blender, blender.On(), blender.Off(), blender.Vzbivaet())
    meat = MeatGrinder("Знамя", "г. Кизел, ул. Доярки 69")
    print(meat, meat.On(), meat.Off(), meat.Rubit())
    print("\nЗАДАНИЕ 2:")
    frigate = Frigate("Ломоносоff", "Военный", 10000)
    print(frigate.On(), frigate.Storoj(), frigate.Off(), frigate.Dead())
    esmin = Destroyer("Ленин", "Военный", 5000)
    print(esmin.On(), esmin.Ebosh(), esmin.Dead())
    cruis = Cruiser("Аврора", "Памятник", 12000)
    print(cruis.On(), cruis.Ogon(), cruis.Off())
    print("\nЗАДАНИЕ 3:")
    money = Money()
    print(money)
    money.addRub()
    money.addKop()
    print(money)

if __name__ == "__main__": main()
