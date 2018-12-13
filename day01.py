#!/usr/bin/env python

import sys, itertools

deltas = [int(line.strip()) for line in sys.stdin]

print "sum:", sum(deltas)

current = 0
freqs = set([current])
for delta in itertools.cycle(deltas):
    current += delta
    if current in freqs:
        print "duplicate:", current
        break
    freqs.add(current)
