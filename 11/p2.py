#!/usr/bin/env python3

import argparse

import pytest


def neighbour_seats(m, x, y):
  occupied = 0
  for dir_x in range(-1, 2):
    for dir_y in range(-1, 2):
      if dir_x == 0 and dir_y == 0:
        continue
      x_cpy = x
      y_cpy = y
      while True:
        x += dir_x
        y += dir_y
        if x < 0 or x >= len(m[0]) or y < 0 or y >= len(m):
          break
        if m[y][x] == '#':
          occupied += 1
          break
        elif m[y][x] == 'L':
          break
      x = x_cpy
      y = y_cpy
  return occupied


def count_occupied_seats(m):
  occupied_seats = 0
  for y in range(len(m)): 
    for x in range(len(m[0])):
      if m[y][x] == '#':
        occupied_seats += 1
  return occupied_seats
      

def task(s: str) -> int:
  m = s.splitlines()

  new = m[:]
  while True:
    for y in range(len(m)):
      for x in range(len(m[0])):
        occupied = neighbour_seats(m, x, y)
        if m[y][x] == 'L' and occupied == 0:
          new[y] = new[y][:x] + '#' + new[y][x+1:]
        elif m[y][x] == '#' and occupied >= 5:
          new[y] = new[y][:x] + 'L' + new[y][x+1:]
    if new == m:  # no change
      return count_occupied_seats(m)
    m = new[:]
        
      
      


INPUT_S = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''


@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 26),
  )
)
def test(inp: str, exp: int) -> None:
  assert task(inp) == exp


def main() -> int:
  parser = argparse.ArgumentParser()
  parser.add_argument('data_file')
  args = parser.parse_args()

  with open(args.data_file) as f:
    print(task(f.read()))

  return 0


if __name__ == '__main__':
  exit(main())
