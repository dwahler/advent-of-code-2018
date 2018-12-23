#!/usr/bin/env python

import sys, itertools, collections
import heapq

depth = 10914
tx = 9
ty = 739

grid = [[0]*(20*ty+1) for i in xrange(20*tx+1)]
M=20183

for y in xrange(20*ty+1):
    grid[0][y] = (y*48271)%M
for x in xrange(1, 20*tx+1):
    grid[x][0] = (x*16807)%M
    for y in xrange(1, 20*ty+1):
        grid[x][y] = ((grid[x-1][y]+depth)*(grid[x][y-1]+depth))%M
grid[tx][ty] = 0

level = [[((e+depth)%M)%3 for e in row] for row in grid]

for y in xrange(11):
    print ''.join(".=|"[level[x][y]] for x in xrange(11))

NONE=0
TORCH=1
GEAR=2
q = [(0,(0,0,TORCH))]
visited = set()

def valid(g,l):
    return (l,g) in [(0,GEAR),(0,TORCH),(1,GEAR),(1,NONE),(2,TORCH),(2,NONE)]

while True:
    t, state = heapq.heappop(q)
    print t, state
    if state in visited:
        continue
    visited.add(state)

    x,y,g = state
    if x == tx and y == ty and g == TORCH:
        print "found",t
        break
    for g2 in [NONE,TORCH,GEAR]:
        if g2 != g and valid(g2,level[x][y]):
            heapq.heappush(q, (t+7, (x,y,g2)))
    for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
        x2 = x + dx
        y2 = y + dy
        if x2 < 0 or y2 < 0 or x2 >= 20*tx or y2 >= 20*ty:
            continue
        if valid(g, level[x2][y2]):
            heapq.heappush(q, (t+1, (x2,y2,g)))
    #print q
