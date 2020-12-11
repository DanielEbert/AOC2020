#!/usr/bin/env python3

import argparse

import pytest


def neighbour_seats(m, x, y):
  occupied = 0
  for pos_x in range(x-1, x+2):
    if pos_x < 0 or pos_x >= len(m[0]):
      continue
    for pos_y in range(y-1, y+2):
      if pos_y < 0 or pos_y >= len(m):
        continue
      if pos_x == x and pos_y == y:
        continue
      if m[pos_y][pos_x] == '#':
        occupied += 1
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
        elif m[y][x] == '#' and occupied >= 4:
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
    (INPUT_S, 37),
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
