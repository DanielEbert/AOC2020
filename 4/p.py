#!/usr/bin/env python3

import argparse

import pytest


def task(s: str) -> int:
  passports_s = s.strip().replace(' ', '\n').split('\n\n')
  valid = 0
  for pp in passports_s:
    required = 6
    if 'cid' in pp:
      required += 1
    if pp.count('\n') >= required:
      valid += 1
  return valid


TEST_INP = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

TEST_INP2 = '''\
ecl:amb hgt:170cm eyr:2025 byr:1930 iyr:2018 hcl:#733820 cid:262
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  [
    (TEST_INP, 2),
    (TEST_INP2, 0)
  ]
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
