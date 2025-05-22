#!/usr/bin/python3

import json

data = {}

def Spisok(x):
    if x > len(data): return
    print(f'ИЛЯ ФАМИЛИЯ ВОЗРАСТ\n')
    if x != 0: print(f'\n')
    else:
        for _ in data:
            print(f'\n')

Spisok(0)
while True:
