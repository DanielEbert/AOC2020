#!/usr/bin/env python3

import argparse

import pytest


def task(s: str) -> int:
  lines = s.splitlines()
  cur_time = int(lines[0])
  ids = [int(i) for i in lines[1].split(',') if i != 'x']
  fastest_time, fastest_id = 100000000000000000000, 0 
  for _id in ids:
     next_time = _id - (cur_time % _id)
     if next_time < fastest_time:
      fastest_time = next_time
      fastest_id = _id
  return fastest_time * fastest_id


INPUT_S = '''\
939
7,13,x,x,59,x,31,19
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 295),
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
