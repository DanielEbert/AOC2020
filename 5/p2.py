#!/usr/bin/env python3

import argparse

import pytest


def binary_search(p, orig_max, left_char, right_char):
  _min = 0
  _max = orig_max
  for i in p:
    mid = _min + (_max - _min) // 2
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
  seat_ids = set()
  for p in s.splitlines():
    row, col = seat_id(p)
    _id = row * 8 + col
    seat_ids.add(_id)
  for _id in seat_ids:
    if _id + 2 in seat_ids and _id + 1 not in seat_ids:
      return _id + 1
    if _id - 2 in seat_ids and _id - 1 not in seat_ids:
      return _id - 1


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
