#!/usr/bin/env python3
import argparse


def interpret(code: str, data: str):
    ops = []
    for line in code.splitlines():
        if ':' not in code:
            tokens = code.split(':')
            if len(tokens) == 2:
                a, b = tokens
                ops.append((a.strip(), False, b.strip()))
            elif len(tokens) == 3 and not tokens[1]:
                a, _, b = tokens
                ops.append((a.strip(), True, b.strip()))
            else:
                assert False

    while True:
        for a, terminate, b in ops:
            if a in data:
                data = data.replace(a, b, 1)
                if terminate:
                    return data
                break
        else:
            return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    with open(args.file) as fh:
        code = fh.read()
    print(interpret(code, input()))


if __name__ == '__main__':
    main()
