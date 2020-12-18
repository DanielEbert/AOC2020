#!/usr/bin/env python3

import argparse
import collections
import re

import pytest

INSTRUCTION_PATTERN = r'mem\[(\d*)\] = (\d*)'

def task(s: str) -> int:
  mem = collections.defaultdict(int)
  programs = s.split('mask = ')[1:]
  for p in programs:
    p = p.splitlines()
    mask = p[0]
    OR_mask = int(mask.replace('X', '0'), 2)
    AND_mask = int(mask.replace('X', '1'), 2)
    for ins in p[1:]:
      addr, val = re.match(INSTRUCTION_PATTERN, ins.strip()).groups()
      addr, val = int(addr), int(val)
      val &= AND_mask
      val |= OR_mask
      mem[addr] = val
  return sum(mem.values())

INPUT_S = '''\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 165),
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
