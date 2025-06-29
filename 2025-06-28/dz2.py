#!/usr/bin/python3

# Класс Герой
class Hero:
    def __init__(self, lvl, name, last_name, lor, history, hp, old, spells, radius, weaknesses, speed, 
                 intelligence, power, agility, lucky, power_damage, exp):
        self.lvl = lvl
        self.name = name
        self.last_name = last_name
        self.lor = lor
        self.history = history
        self.hp = hp
        self.old = old
        self.spells = spells
        self.radius = radius
        self.weaknesses = weaknesses
        self.gender = None
        self.attr = {
            'speed': speed,
            'intelligence': intelligence,
            'power': power,
            'agility': agility,
            'lucky': lucky,
            'power_damage': power_damage,
            'exp': exp
        }

    def atack_to_damage(self): pass

    def protection_to_damage(self): pass

# Класс Противник
class Enemy:
    def __init__(self, attr):
        self.attr = attr

    def atack_to_damage(self): pass

    def protection_to_damage(self): pass


class Log:
    @staticmethod
    def record_battle_result(hero, enemy, result): pass

    @staticmethod
    def analyze_statistics(hero): pass


class Game:
    def __init__(self):
        self.hero = None
        self.enemy = None

    def menu(self):
        # Меню выбора персонажа
        pass

    def battler(self):
        # Цикл боя с врагом
        pass

    def hero_damage_menu_battle(self):
        # Цикл меню для главного героя
        pass
