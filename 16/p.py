#!/usr/bin/env python3

import argparse
import collections
import re

import pytest

FIELD_PATTERN = r'^.*: (\d+)-(\d+) or (\d+)-(\d+)$'

def task(s: str) -> int:
  m = collections.defaultdict(int)
  for field in s.split('\n\n')[0].splitlines():
    assert(re.match(FIELD_PATTERN, field))
    s1, e1, s2, e2 = re.match(FIELD_PATTERN, field).groups()
    ranges = ((int(s1), int(e1)), (int(s2), int(e2)))
    for start, end in ranges:
      for pos in range(start, end+1):
        m[pos] = 1
  # return sum([int(n) for ticket in s.split('\n\n')[2].splitlines()[1:] for n in ticket.split(',') if int(n) not in m])
  # following is same as last line but more readable
  _sum = 0
  for ticket in s.split('\n\n')[2].splitlines()[1:]:
    for n in ticket.split(','):
      n = int(n)
      if n not in m:
        _sum += n
  return _sum
    


INPUT_S = '''\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 71),
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
