#!/usr/bin/env python

import sys, itertools, collections

grid = []
for line in sys.stdin:
    line = line.strip('\n')
    grid.append(list(line))

N = len(grid)
M = len(grid[0])

class Cart(object):
    def __init__(self, x, y, dir):
        self.i = x
        self.j = y
        self.dir = dir
        self.state = 0

# starting from right, ccw
deltai = [0, -1, 0, 1]
deltaj = [1, 0, -1, 0]

deltadir = [1, 0, -1]

carts = {}
next_id = 0
for i in xrange(N):
    for j in xrange(M):
        c = grid[i][j]
        t = {'>': (0,'-'), '^': (1,'|'), '<': (2,'-'), 'v': (3,'|')}.get(c,None)
        if t:
            dir, grid[i][j] = t
            carts[next_id] = Cart(i, j, dir)
            next_id += 1

occupied = dict(((c.i,c.j),i) for (i,c) in carts.items())
while len(carts) >= 2:
    skip = set()
    for id1, cart in sorted(carts.items(), key = lambda (id,c): (c.i,c.j)):
        if id1 in skip:
            continue
        i2 = cart.i + deltai[cart.dir]
        j2 = cart.j + deltaj[cart.dir]
        del occupied[cart.i,cart.j]
        if (i2, j2) in occupied:
            id2 = occupied[i2,j2]
            del occupied[i2,j2]
            skip.add(id1)
            skip.add(id2)
            print "removing", id1, id2, "at", (j2, i2)
            continue

        cart.i = i2
        cart.j = j2
        occupied[cart.i,cart.j] = id1

        c = grid[i2][j2]
        if c == '/':
            cart.dir ^= 1
        elif c == '\\':
            cart.dir = 3-cart.dir
        elif c == '+':
            cart.dir = (cart.dir + deltadir[cart.state%3] + 4) % 4
            cart.state += 1
    for id in skip:
        del carts[id]

print "final", [(c.j,c.i) for c in carts.values()]
