#!/usr/bin/env python

import sys, itertools, collections

data = [int(x) for x in sys.stdin.read().split()]

Node = collections.namedtuple('Node', 'metadata children')

pos = 0
def get():
    global pos
    if pos == len(data):
        return None
    x = data[pos]
    pos += 1
    return x

def read_node():
    nc = get()
    nm = get()
    children = []
    for i in xrange(nc):
        children.append(read_node())
    metadata = []
    for i in xrange(nm):
        metadata.append(get())
    return Node(metadata, children)

def sum_m(node):
    return sum(node.metadata) + sum(sum_m(n) for n in node.children)

def value(node):
    if node.children:
        x = 0
        for i in node.metadata:
            i -= 1
            if 0 <= i < len(node.children):
                x += value(node.children[i])
        return x
    else:
        return sum(node.metadata)
root = read_node()
print sum_m(root)

print value(root)
