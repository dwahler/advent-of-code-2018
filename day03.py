#!/usr/bin/env python

import sys, itertools, collections


grid = [[0]*1000 for i in xrange(1000)]
claims = []

for line in sys.stdin:
    line = line.strip()
    a, rest = line.split('@')
    b, c = rest.split(':')

    left, top = [int(x.strip()) for x in b.split(',')]
    width, height = [int(x.strip()) for x in c.split('x')]

    for i in xrange(top, top+height):
        for j in xrange(left, left+width):
            grid[i][j] += 1
    claims.append((a, left, top, left+width-1, top+height-1))

n = 0
for row in grid:
    for col in row:
        if col > 1:
            n += 1
print n


for a, ax1, ay1, ax2, ay2 in claims:
    overlaps = False
    for b, bx1, by1, bx2, by2 in claims:
        if a == b: continue
        if not ((ax1 > bx2) or (bx1 > ax2) or (ay1 > by2) or (by1 > ay2)):
            overlaps = True
            break
        if overlaps: break
    if not overlaps:
        print a

