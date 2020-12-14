#!/usr/bin/env python3

import argparse

import pytest


def task(s: str) -> int:
  x, y = 10, 1
  s_x, s_y = 0, 0
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
      for _ in range(val//90):
        x, y = -y, x
    elif action == 'R':
      for _ in range(val//90):
        x, y = y, -x
    elif action == 'F':
      s_x += val * x
      s_y += val * y
    print('s',s_x, s_y, 'w',x,y)
  return abs(s_x) + abs(s_y)


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
    (INPUT_S, 286),
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
