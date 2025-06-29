#!/usr/bin/python3

class Hero:
    def __init__(self, lvl, name, last_name, lor, history, hp, old, spells, radius, weaknesses, speed, intelligence, power, agility, lucky, power_damage, exp):
        self.lvl = lvl #Уровень,
        self.name = name #имя,
        self.last_name = last_name # прозвище,
        self.lor = lor #происхождение;
        self.history = history #Принадлежность,
        self.hp = hp #Здоровье,
        self.old = old #возраст,
        self.spells = spells #Умения и способности,
        self.radius = radius#Радиус поражения/атаки,
        self.weaknesses = weaknesses #Слабые стороны(список, словарь),
        self.gender = None #ПОЛ??
        self.attr = {'speed':speed, #Скорость,
            'intelligence': intelligence, #интеллект,
            'power':power, #сила,
            'agility':agility, #ловкость,
            'lucky':lucky, #удача,
            'power_damage':power_damage, #сила атаки,
            'exp':exp #опыт,
        }

    def __str__(self):
        return f"Уровень: {self.lvl}\nИмя: {self.name}\nПрозвище: {self.last_name}\nПроисхождение: {self.lor}\nПринадлежность: {self.history}\nЗдоровье: {self.hp}\nВозраст: {self.old}\nУмения и способности: {self.spells}\nРадиус атаки: {self.radius}\nСлабые стороны: {self.weaknesses}\nПоказатели: {self.attr}"

    def atack_to_damage(self, udar): #Атака персонажа
        self.hp -= udar

    def protection_to_damage(self): #Защита персонажа
        pass

