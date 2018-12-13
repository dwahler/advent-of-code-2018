#!/usr/bin/env python

import sys, itertools, collections

mins = collections.defaultdict(lambda: [0]*60)

lines = []
current_id = None
for line in sys.stdin:
    line = line.strip()
    lines.append(line)

lines.sort()
for line in lines:
    if 'begins shift' in line:
        a, b = line.split('#')
        c = b.split(' ')
        current_id = int(c[0])
        
    else:
        t = int(line[15:17])
        if 'falls asleep' in line:
            sleep = t
        elif 'wakes up' in line:
            wake = t
            print current_id, "sleeping", sleep, wake
            for i in xrange(sleep, wake):
                mins[current_id][i] += 1

guard_id = max(mins, key = lambda x: sum(mins[x]))
counts = mins[guard_id]
minute = max(xrange(len(counts)), key = lambda x: counts[x])
print guard_id, minute, guard_id*minute

a = max([(mins[guard_id][i], guard_id, i) for guard_id in mins for i in xrange(60)])
print a
print a[1]*a[2]
