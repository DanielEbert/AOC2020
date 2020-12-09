#!/usr/bin/env python3

import argparse

import pytest


def task(s: str) -> int:
  ins = []
  for line in s.splitlines():
    op, arg = line.split()
    ins.append((op, int(arg)))
  acc = 0
  ip = 0
  seen = {0}
  while True:
    op, arg = ins[ip]
    if op == 'acc':
      ip += 1
      acc += arg
    elif op == 'jmp':
      ip += arg
    elif op == 'nop':
      ip += 1
    if ip in seen:
      return acc
    seen.add(ip)
  raise Exception('unreachable')


INPUT_S = '''\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 5),
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
