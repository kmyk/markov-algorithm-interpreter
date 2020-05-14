#!/usr/bin/env python3
import argparse
import itertools
import sys
import time
from typing import *


def parse(code: str) -> List[Tuple[str, bool, str]]:
    ops = []
    for line in code.splitlines():
        if ':' not in line:
            continue
        tokens = line.split(':')
        if len(tokens) == 2:
            a, b = tokens
            ops.append((a.strip(), False, b.strip()))
        elif len(tokens) == 3 and not tokens[1]:
            a, _, b = tokens
            ops.append((a.strip(), True, b.strip()))
        else:
            print('failed to parse op:', line, file=sys.stderr)
            sys.exit(1)
    return ops


def apply(ops: List[Tuple[str, bool, str]], data: str) -> Tuple[str, bool]:
    for a, terminate, b in ops:
        if a in data:
            data = data.replace(a, b, 1)
            return data, terminate
    return data, True


def interpret(code: str,
              data: str,
              *,
              limit: Optional[int] = 9999,
              wait: float = 0.0) -> str:
    ops = parse(code)
    print(f'ops = {ops}', file=sys.stderr)
    for step in itertools.count():
        print(f'{step}: {data}', file=sys.stderr)
        if limit is not None and step >= limit:
            break
        data, terminate = apply(ops, data)
        if terminate:
            break
        time.sleep(wait)
    print(f'{step}: {data}', file=sys.stderr)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-l', '--limit', type=int, default=None)
    parser.add_argument('-w', '--wait', type=float, default=0.05)
    args = parser.parse_args()

    with open(args.file) as fh:
        code = fh.read()
    print(interpret(code, input(), limit=args.limit, wait=args.wait))


if __name__ == '__main__':
    main()
