#!/usr/bin/env python3

import argparse

import pytest


def task(s: str) -> int:
  direction = 1  # N=0, E=1, S=2, W=3
  x, y = 0, 0
  for line in s.splitlines():
    action, val = line[0], int(line[1:])
    if action == 'N':
      y += val
    elif action == 'E':
      x += val
    elif action == 'S':
      y -= val
    elif action == 'W':
      x -= val
    elif action == 'L':
      direction = (direction - (val / 90)) % 4
    elif action == 'R':
      direction = (direction + (val / 90)) % 4
    elif action == 'F':
      if direction == 0:
        y += val
      elif direction == 1:
        x += val
      elif direction == 2:
        y -= val
      elif direction == 3:
        x -= val
    print(x,y, direction)
  return abs(x) + abs(y)


INPUT_S = '''\
F10
N3
F7
R90
F11
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 25),
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
