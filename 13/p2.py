#!/usr/bin/env python3

import argparse
from math import gcd

import pytest


def task(s: str) -> int:
  lines = s.splitlines()
  ids = []
  cnt = 0
  for i in lines[1].split(','):
    if i != 'x':
      ids.append((int(i)+cnt, cnt))
      print(i, cnt)
    cnt += 1

  cur_gcd = ids[0][0]
  cur_mlt = ids[0][0]

  for i, cnt in ids[1:]:
    cur_mlt *= i
    cur_gcd = gcd(cur_gcd, i)

  return cur_mlt #// cur_gcd


  #5,3,2
  #5,10,15,20        (4)
  #3,6,9,12,15,18,21 (7)

  #5,(3+1),(2+2)


  # 7,2(3)
  # 7, 14
  # 2,4,8,10,12,14



INPUT_S = '''\
1
7,13,x,x,59,x,31,19
'''

INPUT_S2 = '''\
1
17,x,13,19
'''

INPUT_S3 = '''\
1
67,7,59,61
'''

INPUT_S4 = '''\
1
67,x,7,59,61
'''

INPUT_S5 = '''\
1
67,7,x,59,61
'''

INPUT_S6 = '''\
1
1789,37,47,1889
'''

INPUT_S7 = '''\
1
5,3,2
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 1068781),
    (INPUT_S2, 3417),
    (INPUT_S3, 754018),
    (INPUT_S4, 779210),
    (INPUT_S5, 1261476),
    (INPUT_S6, 1202161486),
    (INPUT_S7, 80),
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
