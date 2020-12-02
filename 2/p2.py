#!/usr/bin/env python3

import argparse
from collections import Counter

import pytest


def task(s: str) -> int:
  lines = s.strip().split('\n')
  valid = 0
  for line in lines:
    left_half = line.split(':')[0]
    nums = left_half.split(' ')[0]
    pos1, pos2 = nums.split('-')
    pos1 = int(pos1) - 1
    pos2 = int(pos2) - 1
    char = left_half.split(' ')[1]
    pw = line.split(':')[1].strip()
    if pos1 >= len(pw) or pos2 >= len(pw):
      continue
    occurances = 0
    if pw[pos1] == char:
      occurances += 1
    if pw[pos2] == char:
      occurances += 1
    if occurances == 1:
      print(occurances, line)
      valid += 1
  return valid


@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    ('1-2 a: a', 0),
    ('1-2 a: ab', 1)
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
