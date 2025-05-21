#!/usr/bin/python3

import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BLACKSIDE = 'blackside'

def main():
    print("Добро пожаловать в игру БлекДжек!")
    print("Правила игры: ")
    money = 5000
    while True:
        if money <= 0:
            print("Ты проиграл все свои деньги!")
            sys.exit()
        print(f"Money: {money}")
        #Ставка игрока на раунд
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(),deck.pop()]
        #бработка действий игрока:
        print(f"Ваша ставка: {bet}")
        while True: #будем продолжать цикл, пока у игрока не будет перебор
        # или он не скажет хватит
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)
            if move == "D":
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f"Ставка удвоена: {bet}")
            if move in ('H','D'):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"Вам выпала {rank , suit} ")
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ('S','D'):
                break
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Диллер берет карту...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break
                input("Нажмите enter для продолжения....")
                print('\n\n')
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print(f"Диллер перебрал! Ты выйграл {bet}!!!")
            money += bet
        elif (playerValue >21) or (playerValue < dealerValue):
            print("Ты проиграл!!!")
            money -= bet
        elif playerValue > dealerValue:
            print(f"Диллер недобрал! Ты выйграл {bet}!!!")
            money += bet
        elif playerValue == dealerValue:
            print("У вас Ничья...")
        input("Нажмите Enter, чтобы продолжить....")
        print('\n\n')

def displayHands(playerHand, dealerHand, showDealerHand):
    # Отображаем карты игрока и диллера. Скрываем первую карту дилера,
    # если showDealerHand равно False.
    print()
    if showDealerHand:
        print(f"ДИЛЛЕР: {getHandValue(dealerHand)}")
        displayCards(dealerHand)
    else:
        print(f"ДИЛЛЕР: ???")
        displayCards([BLACKSIDE] + dealerHand[1:])
    print(f"Игрок: {getHandValue(playerHand)}")
    displayCards(playerHand)

def getHandValue(cards):
    #Вернем стоимость карт. Фигурные карты стоят 10, тузы - 11 или 1.
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ('K',"Q","J"):
            value += 10
        else:
            value += int(rank)
    #Добавляем стоимость тузов
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

#Функция создания колоды
def getDeck():
    deck = []
    #Вернуть список кортежей(номинал, масть) для всех 52 карт
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit)) #добавляем числовые карты
        for rank in ('J','Q','K','A'):
            deck.append(((rank), suit)) #Добавляем старшие карты
    random.shuffle(deck) #тасуем
    return deck

#Функция для ставки
def getBet(maxBet):
    while True:
        #Спрашиваем игрока, сколько он ставит на этот раунд
        print(f"Вы можете поставить от 1 до {maxBet}, пропуск - QUIT")
        bet = input('--> ').upper().strip()
        if bet == "QUIT":
            print("Спасибо за игру!")
            sys.exit()
        if not bet.isdecimal():
            continue #Если игрок не ответил
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def displayCards(cards):
    rows = ['', '', '', '', ''] # Отображаемый в каждой строке текст.

    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Выводим верхнюю строку карты.
        if card == BLACKSIDE:
        # Выводим рубашку карты:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
         # Выводим лицевую сторону карты:
         rank, suit = card # Карта — структура данных типа кортеж.
         rows[1] += '|{} | '.format(rank.ljust(2))
         rows[2] += '| {} | '.format(suit)
         rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

     # Выводим все строки на экран:
    for row in rows:
        print(row)

"""Спрашиваем, какой ход хочет сделать игрок, и возвращаем 'H', если он
219. хочет взять еще карту, 'S', если ему хватит, и 'D', если он удваивает."""
def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move  # Игрок сделал допустимый ход.
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Игрок сделал допустимый ход.

if __name__ == '__main__': main()
