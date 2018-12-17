#!/usr/bin/env python

import sys, itertools, collections
import re

pattern = re.compile(r'([xy])=(\d+), [xy]=(\d+)..(\d+)')

blocks = []
sys.setrecursionlimit(10000)

for line in sys.stdin:
    line = line.strip()
    m = pattern.match(line)
    a, b, c = map(int, [m.group(i) for i in (2,3,4)])
    if m.group(1)=='x':
        blocks.append((a, b, a, c))
    else:
        blocks.append((b, a, c, a))

xs = [i[0] for i in blocks]+[i[2] for i in blocks]
ys = [i[1] for i in blocks]+[i[3] for i in blocks]
xmin = min(xs)-1
ymin = min(min(ys), 0)
xmax = max(xs)+1
ymax = max(ys)

w = xmax-xmin+2
h = ymax-ymin+1

board = [[' ']*w for i in xrange(h)]
for a,b,c,d in blocks:
    for x in xrange(a,c+1):
        for y in xrange(b,d+1):
            board[y-ymin][x-xmin] = '#'

def traverse(x,y):
    if y >= h or x < 0 or x >= w:
        return '|'
    if board[y][x] != ' ':
        return board[y][x]
    c = traverse(x, y+1)
    if c == '|':
        board[y][x] = '|'
        print "(%d,%d) = |" % (x,y)
        return '|'
    
    left_open = False
    for x2 in xrange(x-1, -2, -1):
        if x2 >= 0 and board[y][x2] == '#':
            break
        c = traverse(x2, y+1)
        if c == '|':
            left_open = True
            x2-=1
            break
    right_open = False
    for x3 in xrange(x+1, w+1):
        if x3 < w and board[y][x3] == '#':
            break
        c = traverse(x3, y+1)
        if c == '|':
            right_open = True
            x3+=1
            break

    if left_open or right_open:
        result = '|'
    else:
        result = '~'
    for i in xrange(x2+1, x3):
        board[y][i] = result
    print "(%d-%d,%d) = %s" % (x2+1, x3, y, result)
    return result

traverse(500-xmin, 0-ymin)

n = n2 = 0
for i in xrange(min(ys),ymax+1):
    for j in xrange(xmin,xmax+1):
        c = board[i-ymin][j-xmin]
        if c in ('~','|'):
            n += 1
        if c == '~':
            n2 += 1
    print ''.join(board[i-ymin])
print
print n
print n2
