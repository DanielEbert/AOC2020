#!/usr/bin/env python3

import argparse
import re

import pytest

def validate_field(field) -> bool:
  key, val = field.split(':')
  if key == 'byr':
    if len(val) == 4 and int(val) >= 1920 and int(val) <= 2002:
      return True
  if key == 'iyr':
    if len(val) == 4 and int(val) >= 2010 and int(val) <= 2020:
      return True
  if key == 'eyr':
    if len(val) == 4 and int(val) >= 2020 and int(val) <= 2030:
      return True
  if key == 'hgt':
    if val[-2:] == 'cm' and int(val[:-2]) >= 150 and int(val[:-2]) <= 193:
      return True
    if val[-2:] == 'in' and int(val[:-2]) >= 59 and int(val[:-2]) <= 76:
      return True
  if key == 'hcl':
    if val[0] == '#' and re.match('^[0-9a-f]{6}$', val[1:]):
      return True
  if key == 'ecl':
    if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
      return True
  if key == 'pid':
    if re.match('^[0-9]{9}$', val):
      return True


def task(s: str) -> int:
  passports_s = s.strip().replace(' ', '\n').split('\n\n')
  valid = 0
  for pp in passports_s:
    required = 7

    for field in pp.split('\n'):
      if validate_field(field):
        required -= 1

    if required == 0:
      valid += 1
  return valid


TEST_INP = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

TEST_INP2 = '''\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''

@pytest.mark.parametrize(
  ('inp', 'exp'),
  [
    (TEST_INP, 0),
    (TEST_INP2, 4)
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
