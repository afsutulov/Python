#!/usr/bin/python3

import random

#Класс-Родитель для всех классов в игре
class Class_Hero:
    def __init__(self, Speed, Intelligence, Strength, Agility, Luck, Attack_Power):
        self.Speed = Speed
        self.Intelligence = Intelligence
        self.Agility = Agility
        self.Luck = Luck
        self.Attack_Power = Attack_Power
        self.Strength = Strength
        self.Actions = [self.Jump, self.Move, self.Attack, self.Deffence]

    def Jump(self): pass

    def Move(self): pass

    def Attack(self): pass

    def Deffence(self): pass

#NPC - Базовый класс с параметрами для игровых персонажей и врагов
class NPC:
    def __init__(self, Attack_Power=10, HP=100, enemy_name=''):
        self.Attack_Power = Attack_Power
        self.HP = HP
        self.Enemy_Name = enemy_name

class Enemy(NPC):
    def __init__(self):
        self.enemy_list = ['Гоблин','Куб-Слизь','Дракон','Повелитель телей']
        NPC.__init__(self, random.randint(50,100),random.randint(100,200),self.enemy_list[random.randint(0,len(self.enemy_list)-1)])
    #Получение урона
    def DEFF(self,value_damage):
        self.HP -= value_damage
        if self.HP <= 0:
            return f' {self.Enemy_Name} был убит.'
        return f"{self.Enemy_Name} получил {value_damage} урона. Сейчас у него {self.HP} HP."
    #Нанесение урона
    def ATTACK(self):
        return self.Attack_Power

#Класс для реализации Лучника
class Archer(Class_Hero,NPC):
    def __init__(self, Speed = 1, Intelligence =2, Strength=1, Agility=5, Luck=1, Attack_Power=5, name=''):
        Class_Hero.__init__(self,Speed,Intelligence, Strength, Agility, Luck,Attack_Power)
        NPC.__init__(self,enemy_name=name)
        self.Ability = [self.Shot_Arche, self.Dodge,self.Ultimate] #Список способностей
    def Shot_Arche(self):
        pass
    def Dodge(self):
        pass
    def Ultimate(self):
        pass

#Класс для реализации Целителя
class Healer(Class_Hero,NPC):
    def __init__(self,Speed = 0,Intelligence =5, Strength=0, Agility=2, Luck=0,Attack_Power=1,name=''):
        Class_Hero.__init__(self,Speed,Intelligence, Strength, Agility, Luck,Attack_Power)
        NPC.__init__(self,enemy_name=name)
        self.Ability = [self.Attack_middle, self.Heal, self.Ultimate]  # Список способностей
    def Heal(self):
        pass
    def Attack_middle(self):
        pass
    def Ultimate(self):
        pass

#Класс для реализации Мага
class Mage(Class_Hero,NPC):
    def __init__(self,Speed = 3,Intelligence =10, Strength=0, Agility=8, Luck=3,Attack_Power=8,name=''):
        NPC.__init__(self,enemy_name=name)
        Class_Hero.__init__(self,Speed,Intelligence, Strength, Agility, Luck,Attack_Power)
        self.Ability = [self.FireBoll, self.Magic_Shild, self.Ultimate]  # Список способностей
    def FireBoll(self):
        pass
    def Ultimate(self):
        pass
    def Magic_Shild(self):
        pass

#Класс для реализации Воина
class Warrior(Class_Hero,NPC):
    def __init__(self,Speed = 4,Intelligence =-1, Strength=10, Agility=1, Luck=3,Attack_Power=8,name=''):
        Class_Hero.__init__(self,Speed,Intelligence, Strength, Agility, Luck,Attack_Power)
        NPC.__init__(self,enemy_name=name)
        self.Ability = [self.Attack_Sword, self.Deffence_Shild, self.Ultimate]  # Список способностей
    def Ultimate(self):
        pass
    def Deffence_Shild(self):
        pass
    def Attack_Sword(self):
        pass

#Класс-Меню_Выбора_Персонажа
class Game_Select_Hero:
    def __init__(self):
        self.name = ''
        self.type = ''
    def Hero_Select_User(self):
        self.name = input("Введите Имя:")
        self.type = int(input("Выберите класс персонажа: \n 1.Лучник. \n 2.Целитель \n 3.Маг \n 4.Воин \n Ваш Выбор:"))
        return [self.name, self.type]
    def User_Hello(self):
        print("Добро пожаловать в наш игровый мир по вселенной DND! \n"
              "Cейчас мы отправимся в подземелье, в котором у нас будем много приключений и опасностей! \n"
              "Ваша задача - выбрать класс персонажа и побеждать врагов!"
              "Готовы? тогда приступим! Ответьте на пару вопросов перед игрой:")

#Класс-Меню_Игрового_Процесса
class Game_Process_Change:
    def game(self):
        self.Hero = ''
        gameSelectHero = Game_Select_Hero()  # Создаем конструктор для пользователя
        gameSelectHero.User_Hello()
        herolist = gameSelectHero.Hero_Select_User() #Спрашиваем имя и класс
        #Проверяем создание класса
        match(herolist[1]):
            case 1:
                self.Hero = Archer(name=herolist[0])
            case 2:
                self.Hero = Healer(name=herolist[0])
            case 3:
                self.Hero = Mage(name=herolist[0], )
            case 4:
                self.Hero = Warrior(name=herolist[0], )
        print("Персонаж успешно создан!")

        self.Game_Start = True
        while self.Game_Start:
            enemy = Enemy()
            print(f"Вы идете по коридору и встречаете: {enemy.Enemy_Name} \n Завязался бой!")

#MAIN Для запуска
def main():
    gameprocesschange = Game_Process_Change()
    gameprocesschange.game()

if __name__ == "__main__": main()
