#!/usr/bin/env python3

import argparse
import collections

import pytest


def task(s: str) -> int:
  d = collections.defaultdict(list)
  nums = s.split(',')
  num = None
  for cnt in range(len(nums)):
    num = int(nums[cnt])
    d[num].append(cnt)
  cnt = len(nums)
  while cnt <= 30000000-1:
    if len(d[num]) < 2: 
      d[0].append(cnt)
      num = 0
    else:
      num = d[num][-1] - d[num][-2]
      d[num].append(cnt)
    cnt += 1
  return num


@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    ('0,3,6', 436),
    #('1,3,2',1),
    #('2,1,3',10),
    #('1,2,3',27),
    #('2,3,1',78),
    #('3,2,1',438),
    #('3,1,2',1836),
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
