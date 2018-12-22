#!/usr/bin/env python

def succ(v):
    A = v | 65536
    v = 2176960
    while True:
        v += (A & 255)
        v &= 0xffffff
        v *= 65899
        v &= 0xffffff
        if A < 256:
            return v
        A /= 256

#print succ(7156989)
#succs = [succ(i) for i in xrange(0x1000000)]
visited = set()
i = 0
while i not in visited:
    print i
    visited.add(i)
    i = succ(i)
print "repeat:", i
