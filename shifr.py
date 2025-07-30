#!/usr/bin/python3

import sys

if len(sys.argv) != 2: print("Программа Шифр 1.0. Распространяется свободно. 2025 год\n\nshifr.py [шифруемый_файл]"); exit()
key = {0: 3, 1: 6, 2: 8, 3: 0, 4: 7, 5: 9, 6: 1, 7: 4, 8: 2, 9: 5}
with open(sys.argv[1], 'rb') as f: data = f.read()
data = bytearray(data)
for i in range(len(data)):
    if i % len(key) < key[i % len(key)] and i // len(key) * len(key) + key[i % len(key)] < len(data):
        data[i], data[i // len(key) * len(key) + key[i % len(key)]] = data[i // len(key) * len(key)  + key[i % len(key)]], data[i]
    data[i] = 255 - data[i]
with open(sys.argv[1], 'wb') as f: f.write(data)
