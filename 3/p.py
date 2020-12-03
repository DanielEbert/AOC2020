#!/usr/bin/env python3

import argparse

import pytest


def task(s: str) -> int:
  lines = s.strip().split()
  line_len = len(lines[0])
  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  mul = 1
  for slope in slopes:
    pos = slope
    trees = 0
    while pos[1] < len(lines):
      if lines[pos[1]][pos[0] % line_len] == '#':
        trees += 1
      pos = (pos[0] + slope[0], pos[1] + slope[1])
    print(slope, trees)
    mul *= trees
  return mul
    


@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    # test cases
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
