#!/usr/bin/python3

import  random

NUM_DIGITS= 3 #попробуйте задать число от 1-10
MAX_GUESSES = 10 #Попробуйте задать число 1-100
#MAIN
def print_f():
    print("Добро пожаловать в игру <БЕЙГЛЗ>!")
    print("Основная задача игры - угадать 3-х значное"
          "число за 10 попыток.")
    print("Вовремя игры вы можете увидеть подсказки:\n"
          "1) Pico - угадали правильную цифру на неправильном месте \n"
          "2) Fermi - угадали цифру на правильном месте \n"
          "3) Bagels - не угадали цифру + неправильное место")
    print("Желаю успехов в данной игре!")
def getRandomNum():
    number = list("1234567890")
    random.shuffle(number)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(number[i])
    return secretNum
def getClues(guess, secretNum): #Функция для подсказок
    if guess == secretNum:
        return "Вы угадали!!!"
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi") #Число стоит на своем месте
        elif guess[i] in secretNum:
            clues.append("Pico") #Число стоит не на своем месте
    if len(clues) == 0:
        return 'Bagels' #Не угадали числа
    else:
        clues.sort() #
        return ' '.join(clues)

def main():
    print_f()
    while True:
        secretNum = getRandomNum() #Секретное число
        print(secretNum)
        print("Было задуманно число!")
        print(" У тебя есть {} попыток, чтобы угадать его!".format(MAX_GUESSES))
        numGuesses = 1 #Попытки
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Попытка {numGuesses}")
                guess = input("-->")

            #Подсказка
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("Ваши попытки иссякли")
                print(f"Вы должны были угадать число:{secretNum}")
        print("Хотите попробывать еще раз?(y/n)")
        if not input('-->').lower().startswith('y'):
            break
    print("Спасибо за игру!")

if __name__ == '__main__':
    main()
