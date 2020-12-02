#!/usr/bin/env python3

import argparse

import pytest


def task(s: str) -> int:
  pass  


@pytest.mark.parametrize(
  ('inp', 'exp'),
  (
    # test cases
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
