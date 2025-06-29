#!/usr/bin/python3

class Enemy:
    def __init__(self, name, hp, speed, intelligence, power, agility, lucky, power_damage, exp):
        self.name = name
        self.hp = hp
        self.attr = {'speed':speed, #Скорость,
            'intelligence': intelligence, #интеллект,
            'power':power, #сила,
            'agility':agility, #ловкость,
            'lucky':lucky, #удача,
            'power_damage':power_damage, #сила атаки,
            'exp':exp #опыт,
        }

    def __str__(self):
        return f"Имя: {self.name}\nПоказатели: {self.attr}"

    def atack_to_damage(self, udar): #Атака персонажа
        self.hp -= udar

    def protection_to_damage(self): #Защита персонажа
        pass
