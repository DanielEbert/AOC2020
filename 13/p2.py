#!/usr/bin/env python3

import argparse
from math import gcd

import pytest


# chinese remainer theorem from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def task(s: str) -> int:
  lines = s.splitlines()
  n = []
  a = []
  cnt = len(lines) + 1
  for i in lines[1].split(','):
    if i != 'x':
      n.append(int(i))
      a.append(cnt)
    cnt -= 1
  print(n,a)

  return chinese_remainder(n,a) - len(lines) - 1 #// cur_gcd


  #5,3,2
  #5,10,15,20        (4)
  #3,6,9,12,15,18,21 (7)

  #5,(3+1),(2+2)


  # 7,2(3)
  # 7
  # 2,4,8
  
  # x*7 = y*2+1



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

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 1068781),
    (INPUT_S2, 3417),
    (INPUT_S3, 754018),
    (INPUT_S4, 779210),
    (INPUT_S5, 1261476),
    (INPUT_S6, 1202161486),
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
