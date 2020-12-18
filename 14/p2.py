#!/usr/bin/env python3

import argparse
import collections
import re

import pytest

INSTRUCTION_PATTERN = r'mem\[(\d*)\] = (\d*)'

mask_len = len('X1000001X00010110100X0010000111X0100')
pos2mask = []
for i in range(mask_len):
  pos2mask.append(2**i)
print(pos2mask)

def task(s: str) -> int:
  mem = collections.defaultdict(int)
  programs = s.split('mask = ')[1:]
  for p in programs:
    p = p.splitlines()
    num = int(p[0].replace('X', '1'), 2)
    num_no_x = int(p[0].replace('X', '0'), 2)
    mask = p[0][::-1]
    num_addr = 2 ** mask.count('X')
    for ins in p[1:]:
      addr, val = re.match(INSTRUCTION_PATTERN, ins.strip()).groups()
      addr, val = int(addr), int(val)
      addr |= int(p[0].replace('X','0'), 2)
      addr &= int(p[0].replace('0', '1').replace('X', '0'), 2)
      for i in range(num_addr):
        cur = 0
        cur_x = 0
        for j in range(mask_len):
          if mask[j] != 'X':
            continue
          if i & 2 ** cur_x > 0:
            cur += pos2mask[j]
          cur_x += 1
        mem[cur + addr] = val
        print(addr, cur, val)
    print()
  return sum(mem.values())

INPUT_S = '''\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 209), #TODO
    (INPUT_S, 208), #TODO
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
