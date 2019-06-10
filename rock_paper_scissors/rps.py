#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    result = []
    if n == 0:
        return [result]
    for i in range(0, n):
        inner_list = []
        for j in range(0, len(options)):
            inner_list.append([options[j]])
        result.append(inner_list)
    return result

    result.append(rock_paper_scissors(n - 1))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
