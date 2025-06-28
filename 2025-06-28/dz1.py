#!/usr/bin/python3

import abc

class KlassHero(abc.ABC):
    def __init__(self, student_number, average_mark):
        self.student_number = student_number
        self.average_mark = average_mark

    def is_eligible_to_enroll(self):
        return self.average_mark >= 10 # Вообще не улавливаю сути "игры"

    def get_seminars_taken(self):
        return "Ты участвуешь в семинаре!" # Я хз что тут имеется ввиду)

class Hero(KlassHero):
    def __init__(self, student_number, average_mark, speed, intellect, strength, agility, luck, attack_power):
        super().__init__(student_number, average_mark)
        self.speed = speed
        self.intellect = intellect
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.attack_power = attack_power

    @abc.abstractmethod
    def ultimate(self): pass

class Voin(Hero):
    def ultimate(self):
        return "Мощная атака мечом"

    def def_shield(self):
        return "Щит активирован"

    def attack_sword(self):
        return "Атака мечом!"

class Tselitel(Hero):
    def heal(self):
        return "Лечение союзника"

    def attack_middle(self):
        return "Средняя атака"

    def ultimate(self):
        return "Святое восстановление"

class Mag(Hero):
    def ultimate(self):
        return "Магическая буря"

    def fireball(self):
        return "Огненный шар"

    def magic_shield(self):
        return "Магический щит активирован"

class Luchnik(Hero):
    def shot_arche(self):
        return "Выстрел из лука"

    def dodge(self):
        return "Уклонение"

    def ultimate(self):
        return "Град стрел"

class KlassNPC(abc.ABC):
    def __init__(self, level, name, surname, origin, skills, abilities, weaknesses):
        self.level = level
        self.name = name
        self.surname = surname
        self.origin = origin
        self.skills = skills
        self.abilities = abilities
        self.weaknesses = weaknesses

    @abc.abstractmethod
    def attack(self): pass

    @abc.abstractmethod
    def defend(self): pass

    @abc.abstractmethod
    def use_techniques(self): pass

    @abc.abstractmethod
    def use_abilities(self): pass

class NPC(KlassNPC):
    def attack(self):
        return "NPC атакует"

    def defend(self):
        return "NPC защищается"

    def use_techniques(self):
        return "NPC использует технику"

    def use_abilities(self):
        return f"NPC использует способность: {', '.join(self.abilities)}"

class Personazh:
    def __init__(self, hero_class: Hero = None, npc_class: NPC = None):
        self.hero = hero_class
        self.npc = npc_class

def main():
    voin = Voin(12345, 75, 10, 5, 15, 7, 8, 20)
    npc = NPC(3, "Иван", "Темный", "Деревня", ["Укус"], ["Огненное дыхание"], ["Свет"])
    pers = Personazh(hero_class=voin, npc_class=npc)

    print(pers.hero.attack_sword())
    print(pers.npc.use_abilities())

if __name__ == "__main__": main()
