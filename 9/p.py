#!/usr/bin/env python3

import argparse
import collections

import pytest


def task(s: str) -> int:
  lines_s = s.splitlines()
  lines = [int(line) for line in lines_s]
  nums = collections.defaultdict(int)
  i = 0
  for line in lines[:25]:
    i += 1
    nums[line] += 1
  for i, line in enumerate(lines[25:], 25):
    contains = False
    for prev in nums:
      if line - prev in nums and prev * 2 != line:
        contains = True
        # print(line, prev, line-prev, nums)
        break
    if not contains:
      return line
    nums[line] += 1
    nums[lines[i-25]] -= 1
    if nums[lines[i-25]] == 0:
      nums.pop(lines[i-25], None)


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
    (INPUT_S, 127),
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
