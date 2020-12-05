#!/usr/bin/env python3

import argparse

import pytest


def binary_search(p, orig_max, left_char, right_char):
  _min = 0
  _max = orig_max
  for i in p:
    mid = _min + (_max - _min) // 2
    print(i, mid, _min, _max)
    if i == left_char:
      _max = mid
    elif i == right_char:
      _min = mid + 1
  assert(_min == _max)
  return _min


def seat_id(p):
  row = binary_search(p[:7], 127, 'F', 'B')
  column = binary_search(p[7:], 7, 'L', 'R')
  return row, column
  


def task(s: str) -> int:
  cur_max_id = -1
  for p in s.splitlines():
    row, col = seat_id(p)
    _id = row * 8 + col
    cur_max_id = max(cur_max_id, _id)
  return cur_max_id



@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    ('FBFBBFFRLR', (44, 5)),
    ('BFFFBBFRRR', (70, 7)),
    ('FFFBBBFRRR', (14, 7)),
    ('BBFFBBFRLL', (102, 4)),
  )
)
def test(inp: str, exp) -> None:
  assert seat_id(inp) == exp


def main() -> int:
  parser = argparse.ArgumentParser()
  parser.add_argument('data_file')
  args = parser.parse_args()

  with open(args.data_file) as f:
    print(task(f.read()))

  return 0


if __name__ == '__main__':
  exit(main())
