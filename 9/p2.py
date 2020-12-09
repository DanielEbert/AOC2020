#!/usr/bin/env python3

import argparse
import collections

import pytest


def task(s: str) -> int:
  lines_s = s.splitlines()
  lines = [int(line) for line in lines_s]
  invalid_num = 756008079  # change to 127 for the test
  l = 0
  r = 1
  _sum = lines[l] + lines[r]
  while _sum != invalid_num:
    print(_sum, l, r)
    if _sum < invalid_num:
      r += 1
      _sum += lines[r]
    else:
      _sum -= lines[l]
      l += 1

  count_range = lines[l:r+1]
  return min(count_range) + max(count_range)


INPUT_S = '''\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 62),
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
