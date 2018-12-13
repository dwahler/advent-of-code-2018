#!/usr/bin/env python

import sys, itertools, collections

points = []
for line in sys.stdin:
    line = line.strip()
    x, y = map(int, line.split(', '))
    points.append((x,y))

minx = min(p[0] for p in points)-10
miny = min(p[1] for p in points)-10
maxx = max(p[0] for p in points)+10
maxy = max(p[1] for p in points)+10

counts = collections.defaultdict(int)
infinite = set()

for x in xrange(minx, maxx+1):
    for y in xrange(miny, maxy+1):
        mindist = 999999999
        idx = None
        for i, (x2, y2) in enumerate(points):
            d = abs(x2-x)+abs(y2-y)
            if d < mindist:
                mindist = d
                idx = i
            elif d == mindist:
                idx = None
        if x == minx or x == maxx or y == miny or y == maxy:
            infinite.add(idx)
        if idx is not None:
            counts[idx]+=1

max_value, max_idx = max((counts[i], i) for i in counts if i not in infinite)
print max_value

safe_count=0
for i in xrange(minx, maxx):
    for j in xrange(miny, maxy):
        d = 0
        for i2, j2 in points:
            d += abs(i-i2)+abs(j-j2)
        if d < 10000:
            safe_count += 1
print safe_count
