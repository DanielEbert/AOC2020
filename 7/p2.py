#!/usr/bin/env python3

import argparse
import re
import collections

import pytest

PATTERN = r'^([^ ]+ [^ ]+) bags contain (.+)$'
BAGS = r'(\d+) ([^ ]+ [^ ]+)'

def task(s: str) -> int:
  children = collections.defaultdict(list)
  for line in s.splitlines():
    match = re.match(PATTERN, line)
    assert match, line
    contained_bags = [(int(n), c) for n, c in re.findall(BAGS, match.group(2))]
    children[match.group(1)] = contained_bags
  print(children)
  total = -1
  todo = [(1, 'shiny gold')]
  while todo:
    cur = todo.pop()
    total += cur[0]
    todo.extend(children[cur[1]] * cur[0])
    print(todo)
  return total


INPUT_S = '''\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''

INPUT_S2 = '''\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 32),
    (INPUT_S2, 126),
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
