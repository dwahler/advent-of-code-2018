#!/usr/bin/env python

import sys, itertools, collections

board = []
for line in sys.stdin:
    line = line.strip()
    board.append(list(line))

def step(board):
    N = len(board)
    M = len(board[0])
    result = [[None]*M for i in xrange(N)]

    for i in xrange(N):
        for j in xrange(M):
            counts = collections.Counter()
            for dx in xrange(-1, 2):
                for dy in xrange(-1, 2):
                    if dx == 0 and dy == 0: continue
                    i2 = i+dx
                    j2 = j+dy
                    if 0 <= i2 < N and 0 <= j2 < M:
                        counts[board[i2][j2]]+=1
            if board[i][j] == '.':
                result[i][j] = '|' if counts['|'] >= 3 else '.'
            elif board[i][j] == '|':
                result[i][j] = '#' if counts['#'] >= 3 else '|'
            else:
                result[i][j] = '#' if (counts['#'] >= 1 and counts['|'] >= 1) else '.'
    return result

for i in xrange(10000):
    board = step(board)
    """for row in board:
        print ''.join(row)"""

    if i % 100 == 0:
        counts = collections.Counter()
        for row in board:
            for c in row:
                counts[c]+=1
        print i, counts['#']*counts['|']

