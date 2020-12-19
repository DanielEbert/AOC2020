#!/usr/bin/env python3

import argparse
import collections
import re

import pytest

FIELD_PATTERN = r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$'

def task(s: str) -> int:
  m = collections.defaultdict(set)
  field_set = set()
  for field in s.split('\n\n')[0].splitlines():
    assert(re.match(FIELD_PATTERN, field))
    field_name, s1, e1, s2, e2 = re.match(FIELD_PATTERN, field).groups()
    field_set.add(field_name)
    ranges = ((int(s1), int(e1)), (int(s2), int(e2)))
    for start, end in ranges:
      for pos in range(start, end+1):
        m[pos].add(field_name)
  fields_set = []
  num_fields = '749,494,864,530,921,599,370,550,323,202,821,99,783,496,90,828,65,605,725,745'.count(',') + 1
  for i in range(num_fields):
    fields_set.append(field_set.copy())
  valid_tickets = []
  valid_tickets.append(s.split('\n\n')[1].splitlines()[1])
  for ticket in s.split('\n\n')[2].splitlines()[1:]:
    valid = True
    for n in ticket.split(','):
      n = int(n)
      if n not in m:
        valid = False
        break
    if valid:
      valid_tickets.append(ticket)
  for ticket in valid_tickets:
    for cnt, i in enumerate(ticket.split(',')):
      i = int(i)
      fields_set[cnt] &= m[i]
  singles = [None] * num_fields
  # look for single element fields in fields_set, remove that element from all
  # others until no more 1 fields are there
  def get_singles(s):
    for i in range(len(s)):
      if s[i] != None and len(s[i]) == 1:
        return i
    return None
  while (single := get_singles(fields_set)) != None:
    for i in range(len(fields_set)):
      if i != single and fields_set[i] != None:
        fields_set[i] -= fields_set[single]
    singles[single] = fields_set[single].pop()
    fields_set[single] = None
  ret = 1
  for cnt, i in enumerate(singles):
    if i.startswith('departure'):
      ret *= int(valid_tickets[0].split(',')[cnt])
  return ret
    


INPUT_S = '''\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
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
