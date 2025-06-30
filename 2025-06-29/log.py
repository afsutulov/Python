#!/usr/bin/python3

class Log:
    @staticmethod
    def __init__(name, name2):
        txt = f"Герой: {name}\nПротивник: {name2}\n\nНачинаем игру!"
        print(f"\n{txt}")
        with open('log.txt', 'w') as f: f.write(f"{txt}")

    def damage(self, name, name2, damage_power, hp):
        if hp <= 0: hp = 0
        txt = f"{name} нанес {damage_power} урона {name2}. Здоровье {name2}: {hp}"
        print(f"\n{txt}")
        with open('log.txt', 'a') as f: f.write(f"{txt}\n")

    def pobeda(self, name):
        txt = f"Победил {name}! Игра окончена!"
        print(txt)
        with open('log.txt', 'a') as f: f.write(f"{txt}\n")
        exit()
