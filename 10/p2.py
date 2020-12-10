#!/usr/bin/env python3

import argparse

import pytest


def paths_in_contiguous_ones(n_paths, cur, jolts) -> int:
  stack = [0]
  while stack:
    ind = stack.pop()
    if ind >= len(jolts)-1:
      n_paths += 1
    for i in range(1, 4):
      if ind + i == len(jolts):
        break
      if jolts[ind + i] - jolts[ind] <= 3:
        stack.append(ind + i)
  return n_paths


def task(s: str) -> int:
  jolts = sorted([int(i) for i in s.splitlines()])
  jolts = [0] + jolts + [jolts[-1] + 3]
  paths = 1
  l = 0
  for r in range(len(jolts)):
    if r+1 < len(jolts) and jolts[r+1] - jolts[r] == 1:
      continue
    x = r - l + 1
    lcpy = l
    l = r + 1
    if x <= 2:
      continue
    paths *= paths_in_contiguous_ones(0, 0, jolts[lcpy:r+1])

  return paths


INPUT_S = '''\
16
10
15
5
1
11
7
19
6
12
4
'''

INPUTS_S2 = '''\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 8),
    (INPUTS_S2, 19208),
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
