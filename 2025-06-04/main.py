#!/usr/bin/python3

class Soda:
    def __init__(self, type_add = None):
        self.type_add = type_add
        self.show_my_drink()

    def show_my_drink(self):
        if self.type_add != None: print(f"Газировка и {self.type_add}")
        else: print("Обычная газировка")

class Programmer:
    def __init__(self, name = "", rang = "Junior", chas = 0):
        self.name = name
        self.rang = rang
        self.chas = chas

    def work(self):
        match self.rang:
            case "Junior":  self.chas += 10
            case "Middle":  self.chas += 15
            case "Senior":  self.chas += 20

    def rise(self):
        match self.rang:
            case "Junior":  self.rang = "Middle"
            case "Middle":  self.rang = "Senior"
            case "Senior":  self.chas += 1

    def info(self):
        return f"Программист: {self.name}\tДолжность: {self.rang}\tЗарплата: {self.chas} тубриков"

import random

class NPC:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"Имя: {self.name}, Очки здоровья: {self.hp}"

    def attack(self):
        pass

class Swordsman(NPC):
    def __init__(self, name, hp1, min_damage=0, max_damage=0):
        NPC.__init__(self, name, hp1)
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return f"Мечник {self.name} нанес {random.randint(self.min_damage, self.max_damage)} урона"

class Mage(NPC):
    def __init__(self, name, hp2, mana=0):
        NPC.__init__(self, name, hp2)
        self.mana = mana

    def attack(self):
        if self.mana >0:
            s = f"Маг {self.name} нанес {self.mana*2} урона"
            self.mana -= 20
            return s
        else:
            return "Не могу атаковать, Мана закончилась"

class MSDice:
    def __init__(self, gran):
        self.gran = gran

    def __str__(self):
        return str(random.randint(1, self.gran + 1))

class Player:
    def __init__(self, nickname, exp_points=0, inventory=[]):
        self.nickname = nickname
        self.exp_points = exp_points
        self.inventory = inventory

    def __str__(self):
        return f"Ник: {self.nickname}\tОчков: {self.exp_points}\tСписок предметов: {', '.join(self.inventory)}"

    def addExp(self, exp):
        self.exp_points += exp

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        self.inventory.remove(item)


def main():
#    Soda("Уксус")
#    Soda()
#    a = Programmer("Вася")
#    print(a.info())
#    a.work()
#    print(a.info())
#    a.rise()
#    print(a.info())
#    a.work()
#    print(a.info())
#    a.rise()
#    a.work()
#    print(a.info())
#    a.rise()
#    print(a.info())
#    mage = Mage("Гендальф", 50, 100)
#    print(mage)
#    s = Swordsman("Гомик", 150, 1, 20)
#    print(s)
#    for i in range(2):
#        print(s.attack())
    print(f"{MSDice(20)}\n")

    a = Player("Петя")
    print(a)
    a.addExp(10)
    print(a)
    a.addItem("Клюшка")
    print(a)
    a.addExp(30)
    a.addItem("Маска")
    print(a)
    a.removeItem("Клюшка")
    print(a)


if __name__ == "__main__": main()
