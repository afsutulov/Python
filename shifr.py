#!/usr/bin/python3

import sys

if len(sys.argv) != 2: exit()
key = { 0: 3, 1: 6, 2: 8, 3: 0, 4: 7, 5: 9, 6: 1, 7: 4, 8: 2, 9: 5 }
with open(sys.argv[1], 'rb') as file: data = file.read()
data = bytearray(data)
for i in range(len(data)):
    if i % 10 < key[i % 10] and i // 10 * 10 + key[i % 10] < len(data):
        data[i], data[i // 10 * 10 + key[i % 10]] = data[i // 10 * 10  + key[i % 10]], data[i]
    data[i] = 255 - data[i]
with open(sys.argv[1], 'wb') as file: file.write(data)
