#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import argparse
from sys import stderr, stdin
from reservoir import ReservoirSampling

def build_reservoir(data, R):
    try:
        rs = ReservoirSampling(R)
        result = ''
        # reading stdin input and ignoring "\n" "\r" line-breaks
        for i in data.read().splitlines(): 
            rs.sample(i)
        for i in rs: 
            result += i

    except KeyboardInterrupt:
            print('\n! User interrupted the process, stopping now\n', file=stderr)
    except StopIteration:
            pass
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('size', help="Reservoir size", type=int)
    args = parser.parse_args()
    # calling function to create reservoir using ReservoirSampling object
    for row in build_reservoir(stdin,
                               R=args.size):
        print(row, end="")