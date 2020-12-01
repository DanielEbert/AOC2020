#!/usr/bin/env python3

with open('inp.txt') as f:
  inp = f.read().split('\n')[:-1]

print(inp)

target = 2020
prev_nums = set()

for i in inp:
  i = int(i)
  other = target - i
  if other in prev_nums:
    print('FOUND', i * other)
  prev_nums.add(i)
