#!/usr/bin/env python

import sys, itertools, collections

def diff(a,b):
    n = 0
    for c1, c2 in zip(a,b):
        if c1 != c2:
            n += 1
    return n

words = []

a = b = 0
for line in sys.stdin:
    line = line.strip()
    words.append(line)
    c = collections.Counter(line)
    c2 = set(c.values())
    if 2 in c2:
        a += 1
    if 3 in c2:
        b += 1
print a, b, a*b

for a in words:
    for b in words:
        if diff(a,b) == 1:
            print ''.join(c1 for c1,c2 in zip(a,b) if c1==c2)
