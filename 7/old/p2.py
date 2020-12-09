#!/usr/bin/env python3

import argparse

import pytest


def parse_bag_string(line):
  line = line[:-1]
  parent, child = line.split(' contain ')
  parent = parent[:-4]
  child_bags_s = child.split(', ')
  child_bags = []
  for i in child_bags_s:
    if i.endswith('bag'):
      child_bags.append(i[2:-3])
    elif i.endswith('bags'):
      child_bags.append(i[2:-4])
  return parent, child_bags



def task(s: str) -> int:
  bags = {}
  num_bags = s.strip().count('\n') + 1
  print(f'We have {num_bags} bags')
  #for line in s.strip().split('\n'):
  cnt = 0
  while len(bags) != num_bags:
    cnt += 1
    for line in s.strip().split('\n'):
      parent, child_bags = parse_bag_string(line)
      if parent in bags:
        continue
      if child_bags == [' other ']:
        bags[parent] = [1]
        continue
      _continue = False
      for i in child_bags:
        if i not in bags:
          _continue = True
      if _continue:
        continue
      bags[parent] = []
      for i in child_bags:
        bags[parent].append(i)
        bags[parent].extend(bags[i])
      print(parent, bags[parent])
  shiny_gold_bags = 0
  print(bags['shiny gold '])
  return len(bags['shiny gold '])
        



INPUT_S = '''\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''

INPUT_S2 = '''\
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

@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    (INPUT_S, 126),
    (INPUT_S2, 32),
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
