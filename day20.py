#!/usr/bin/env python

import sys, itertools, collections

regex = raw_input()
regex = regex[1:-1]

i = 0
def peek():
    if i < len(regex):
        return regex[i]
    else:
        return None

def get():
    global i
    c = regex[i]
    i += 1
    return c

Sequence = collections.namedtuple('Sequence', 'seq')
Alternative = collections.namedtuple('Alternative', 'alts')
Literal = collections.namedtuple('Literal', 'dir')

def parse_expr():
    seq = []
    while peek() is not None and peek() in 'NESW(':
        if peek() == '(':
            seq.append(parse_alt())
        else:
            seq.append(Literal(get()))
    return Sequence(seq)

def parse_alt():
    assert get() == '('
    alts = []
    while True:
        alts.append(parse_expr())
        c = get()
        if c == ')':
            break
        assert c == '|'
    return Alternative(alts)

class State(object):
    def __init__(self):
        self.successors = []

allstates = []
def traverse(expr, start):
    current = start
    for e in expr.seq:
        end = State()
        if isinstance(e, Alternative):
            for a in e.alts:
                next = traverse(a, current)
                next.successors.append((None,end))
        elif isinstance(e, Literal):
            current.successors.append((e.dir,end))
        current = end
    return current

"""next_num = 0
visited = set([])
def number(node):
    global next_num
    if node in visited:
        return
    visited.add(node)
    for _, next in node.successors:
        number(next)
    node.index = next_num
    next_num += 1"""

visited = set([])
edges = collections.defaultdict(set)

head = State()
traverse(parse_expr(), head)

stack = [(0,0,head)]
deltas = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}

while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)

    x, y, curstate = current
    for dir, nextstate in curstate.successors:
        if dir is not None:
            dx, dy = deltas[dir]
            x2 = x+dx
            y2 = y+dy

            edges[x,y].add((x2,y2))
            edges[x2,y2].add((x,y))
        else:
            x2 = x
            y2 = y
        stack.append((x2, y2, nextstate))

for k in sorted(edges):
    print k, edges[k]

visited = set([])
queue = [(0,0)]
dist = 0
far = 0
while queue:
    print queue
    nextqueue = []
    for cur in queue:
        if cur in visited:
            continue
        visited.add(cur)
        if dist >= 1000:
            far += 1
        for next in edges[cur]:
            nextqueue.append(next)
    queue = nextqueue
    dist += 1
print dist - 2
print far, "out of", len(edges)
