#!/usr/bin/env python

import sys, itertools, collections

board = []
for line in sys.stdin:
    line = line.strip()
    board.append(list(line))

elfpower = 25

N = len(board)
M = len(board[0])

State = collections.namedtuple('State', 'il jl i0 j0 i j')
hp = {}
n = collections.defaultdict(int)
for i in xrange(N):
    for j in xrange(M):
        if board[i][j] in ('E','G'):
            hp[i,j] = 200# if board[i][j] == 'G' else 1390
            n[board[i][j]] += 1

rounds = 0
while True:
    print "rounds=", rounds, n
    for line in board:
        print ''.join(line)
    print sorted(hp.items())
    print

    starts = []
    for i in xrange(N):
        for j in xrange(M):
            if board[i][j] in ('E','G'):
                starts.append((i,j))

    combat_done = False
    skip = set([])
    for i,j in starts:
        if (i,j) in skip:
            continue
        print i, j, "moving"
        if board[i][j] == '.':
            continue
        queue = [State(i,j,i,j,i,j)]
        visited = set([])
        target = 'E' if board[i][j] == 'G' else 'G'
        if n[target] == 0:
            combat_done = True
            break

        best = None
        dist = 0
        while queue and not best:
            #print queue
            next = []
            for state in sorted(queue):
                if (state.i,state.j,state.i0,state.j0) in visited:
                    continue
                visited.add((state.i,state.j,state.i0,state.j0))
                if board[state.i][state.j] == target:
                    best = state
                    break
                for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    i2 = state.i+di
                    j2 = state.j+dj
                    if 0 <= i2 < N and 0 <= j2 < M and (dist == 0 or board[state.i][state.j] == '.'):
                        if dist == 0:
                            next.append(State(state.i, state.j, i2, j2, i2, j2))
                        else:
                            next.append(State(state.i, state.j, state.i0, state.j0, i2, j2))
            if best is not None:
                break
            queue = next
            dist += 1
        print "dist", dist, "best", state
        if best is None:
            continue

        elif dist > 1:
            i2, j2 = best.i0, best.j0
            print "moving to", i2, j2, "for", state.il, state.jl
            board[i2][j2] = board[i][j]
            board[i][j] = '.'
            hp[i2,j2] = hp[i,j]
            del hp[i,j]
            i,j = i2,j2
            skip.add((i,j))

        bestcell = None
        besthp = (float('inf'),None,None)
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            i2 = i+di
            j2 = j+dj
            if 0 <= i2 < N and 0 <= j2 < M and board[i2][j2] == target:
                if (hp[i2,j2],i2,j2) < besthp:
                    besthp = (hp[i2,j2],i2,j2)
                    bestcell = i2,j2

        if bestcell is not None:
            print "attacking", bestcell
            hp[bestcell] -= 3 if target=='E' else elfpower
            if hp[bestcell] <= 0:
                del hp[bestcell]
                n[board[bestcell[0]][bestcell[1]]] -= 1
                board[bestcell[0]][bestcell[1]] = '.'

        print
    if combat_done:
        break
    rounds += 1
    """
    if rounds > 50:
        break"""


print sorted(n.items())
print rounds, sum(hp.values()), rounds*sum(hp.values())



