#!/usr/bin/env python3

import argparse

import pytest


def task(s: str) -> int:
  jolts = sorted([int(i) for i in s.splitlines()])
  diffs = [0, 0, 1]
  prev = 0
  for i in jolts:
    diffs[i - prev - 1] += 1
    prev = i
  return diffs[0] * diffs[2]


INPUT_S = '''\
16
10
15
5
1
11
7
19
6
12
4
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 7*5),
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
