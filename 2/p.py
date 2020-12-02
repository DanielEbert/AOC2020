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
    min_num, max_num = nums.split('-')
    char = left_half.split(' ')[1]
    pw = line.split(':')[1]
    count = Counter(pw)
    if char not in count:
      continue
    if int(min_num) <= count[char] <= int(max_num):
      valid += 1
  return valid


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
