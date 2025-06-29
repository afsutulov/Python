#!/usr/bin/python3

from heroes import Hero
from enemy import Enemy
from log import Log
import random

class Game:
    @staticmethod
    def num(txt, n1, n2): # Функция ввода и проверки цифры в заданном диапазоне
        _ = input(f'{txt}: ')
        if _.isnumeric() and n1 <= int(_) <= n2: return int(_)
        else: print(f'\u001b[31mОшибка ввода! Необходимо ввести число от {n1} до {n2}!\u001b[0m\n'); return Game.num(txt, n1, n2)

    def menu():

        heroes = (Hero(10, "Маг", "Лохматый", "Колуны", "Аристократ", 100, 56, "Колдует", 100, ("курит", "пьет", "слабый на передок"), 30, 0, 20, 1, 5, 10, 4),
                        Hero(10, "Танк", "ВИ Ленин", "Армия", "Заводчанин", 100, 12, "Давит", 50, ("дизельный", "на летнец резине"), 40, 0, 12, 1, 5, 10, 4),
                        Hero(10, "Воин", "Ржевский", "Пехота", "Из крестьн", 100, 24, "Идет в атаку", 200, ("пьет", "слабый желудок"), 50, 0, 70, 1, 5, 10, 4),
                        Hero(10, "Лучник", "Очко", "Артилерия", "Холоп", 100, 27, "Стреляет", 70, ("трусливый", "слабый на передок"), 60, 0, 40, 1, 5, 10, 4))
        match Game.num("Добро пожаловать в игру!\n\nВсего у нас 4 игровых персонажа:\n\t1. Маг\n\t2. Танк\n\t3. Воин\n\t4. Лучник\n\t0. Выйти их игры\nВаш выбор", 0, 4):
            case 0: exit()
            case 1: hero = Hero(10, "Маг", "Лохматый", "Колуны", "Аристократ", 100, 56, "Колдует", 100, ("курит", "пьет", "слабый на передок"), 30, 0, 20, 1, 5, 10, 4)
            case 2: hero = Hero(10, "Танк", "ВИ Ленин", "Армия", "Заводчанин", 100, 12, "Давит", 50, ("дизельный", "на летнец резине"), 40, 0, 12, 1, 5, 10, 4)
            case 3: hero = Hero(10, "Воин", "Ржевский", "Пехота", "Из крестьн", 100, 24, "Идет в атаку", 200, ("пьет", "слабый желудок"), 50, 0, 70, 1, 5, 10, 4)
            case 4: hero = Hero(10, "Лучник", "Очко", "Артилерия", "Холоп", 100, 27, "Стреляет", 70, ("трусливый", "слабый на передок"), 60, 0, 40, 1, 5, 10, 4)

        match Game.num("Выберите противника:\n\t1. Слизень\n\t2. Гоблин\n\t3. Наблюдатель\n\t4. Орк\n\t0. Выйти их игры\nВаш выбор", 0, 4):
            case 0: exit()
            case 1: enemy = Enemy("Слизень", 100, 30, 0, 20, 1, 5, 10, 4)
            case 2: enemy = Enemy("Гоблин", 100, 40, 0, 12, 1, 5, 10, 4)
            case 3: enemy = Enemy("Наблюдатель", 100, 50, 0, 70, 1, 5, 10, 4)
            case 4: enemy = Enemy("Орк", 100, 60, 0, 40, 1, 5, 10, 4)

        Game.battle(hero, enemy)

    def battle(hero, enemy):
        log = Log(hero.name, enemy.name)
        hod = random.randint(0, 1) # Выбор кто первый ходит: 0 - герой, 1 - противник
        while True:
            if hero.hp <= 0: log.pobeda(enemy.name)
            if enemy.hp <= 0: log.pobeda(hero.name)
            if hod == 0: # Ход героя
                udar = random.randint(0, hero.attr["power_damage"])
                enemy.atack_to_damage(udar)
                log.damage(hero.name, enemy.name, udar, enemy.hp)
            else: # Ход противника
                udar = random.randint(0, enemy.attr["power_damage"])
                hero.atack_to_damage(udar)
                log.damage(enemy.name, hero.name, udar, hero.hp)
            hod = 1 - hod # Смена хода
