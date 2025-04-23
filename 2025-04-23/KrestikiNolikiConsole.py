#!/usr/bin/python3

board = [' '] * 9 # игровая доска
player = 'X' # Ход игрока
game_running = True # Условие для игры
winList = [[0,1,2],[3,4,5],[6,7,8],
           [0,3,6],[1,4,7],[2,5,8],
           [0,4,8],[2,4,6]] # Список комбанаций для победы

def Doska(Flag):
    for _ in range(3):
       print('-' * 9)
       if Flag: print(f'{board[_*3]} | {board[_*3+1]} | {board[_*3+2]}')
       else: print(f'{_*3+1} | {_*3+2} | {_*3+3}')

# Вывод игрового поля
print('Добро пожаловать в игру: Крестики-Нолики!')
print('Играем на поле с выбором клеток:')
Doska(False)
print('\nУдачи и хорошей игры!')

# Игровой процесс
while game_running:
    # Ход игрока
    Doska(True)
    print(f'Ход игрока: {player}')
    while True:
       try:
          position = int(input('Веберете позицию для хода (1-9): ')) - 1
          if 0 <= position <= 8 and board[position] == ' ': break
          else: print('Некорректный ход. Обдумайте еще раз!')
       except ValueError:
          print('Попробуйте ввести числов от 1-9!!!')
    board[position] = player
    # Проверка на победителя
    for combo in winList:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
           game_running = False
           break
    # Проверка на ничью
    if ' ' not in board: game_running = False
    if game_running:
       if player == 'X': player = '0'
       else: player = 'X'

# Вывести финальную доску
print('\nФинальная доска')
Doska(True)
print(f'Победил игрок: {player}!!!')
else: print('Игра закончилась ничьей!')
