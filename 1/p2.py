#!/usr/bin/env python3

with open('inp.txt') as f:
  inp = f.read().split('\n')[:-1]

target = 2020

inp = [int(i) for i in inp]

for i1, a in enumerate(inp):
  for i2, b in enumerate(inp):
    for i3, c in enumerate(inp):
      if i1 == i2 or i1 == i3 or i2 == i3:
        continue
      if a + b + c == target:
        print('FOUND', a * b * c, i1, i2, i3)
