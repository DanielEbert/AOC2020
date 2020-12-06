#!/usr/bin/env python3

import argparse

import pytest

from collections import Counter


def task(s: str) -> int:
  grps = s.strip().split('\n\n')
  cnt = 0
  for grp in grps:
    c = Counter(grp.replace('\n', ''))
    print(c, len(c))
    cnt += len(c)
  return cnt 
    

TEST_INP = '''\
abc

a
b
c

ab
ac

a
a
a
a

b
'''


@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (TEST_INP, 11),
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
