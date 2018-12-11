#!/usr/bin/env python

import sys, itertools, collections

t = int(sys.argv[1])

points = []
for line in sys.stdin:
    line = line.strip()
    x = int(line[10:16].strip())
    y = int(line[18:24].strip())
    vx = int(line[36:38].strip())
    vy = int(line[40:42].strip())
    points.append((x+t*vx, y+t*vy))

x0 = min(p[0] for p in points)
x1 = max(p[0] for p in points)+1
y0 = min(p[1] for p in points)
y1 = max(p[1] for p in points)+1

rows = [[' ']*(x1-x0) for i in xrange(y0, y1)]
for x,y in points:
    rows[y-y0][x-x0] = '#'

print y1-y0
for row in rows:
    print ''.join(row)
