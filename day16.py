#!/usr/bin/env python

import sys, itertools, collections

lines = []

for line in sys.stdin:
    line = line.strip('\n')
    lines.append(line)

cases = []
it = iter(lines)
while True:
    a = next(it)
    if not a:
        break
    b = next(it)
    c = next(it)

    before = map(int, a.split(':')[1].strip(' []').split(', '))
    op = map(int, b.split())
    after = map(int, c.split(':')[1].strip(' []').split(', '))
    
    cases.append((before, op, after))

    next(it)

program = []
while True:
    try:
        l = next(it)
    except StopIteration:
        break
    if not l: continue
    program.append(map(int,l.split()))
print len(program)

def addr(a, b, c, regs):
    regs[c] = regs[a]+regs[b]

def addi(a, b, c, regs):
    regs[c] = regs[a] + b

def mulr(a,b,c,regs):
    regs[c] = regs[a]*regs[b]
def muli(a,b,c,r):
    r[c]=r[a]*b
def banr(a,b,c,r):
    r[c]=r[a]&r[b]
def bani(a,b,c,r):
    r[c]=r[a]&b
def borr(a,b,c,r):
    r[c]=r[a]|r[b]
def bori(a,b,c,r):
    r[c]=r[a]|b
def setr(a,b,c,r):
    r[c]=r[a]
def seti(a,b,c,r):
    r[c]=a
def gtir(a,b,c,r):
    r[c]=int(a>r[b])
def gtri(a,b,c,r):
    r[c]=int(r[a]>b)
def gtrr(a,b,c,r):
    r[c]=int(r[a]>r[b])
def eqir(a,b,c,r):
    r[c]=int(a==r[b])
def eqri(a,b,c,r):
    r[c]=int(r[a]==b)
def eqrr(a,b,c,r):
    r[c]=int(r[a]==r[b])

ops = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

threecount = 0
allnames = [f.func_name for f in ops]
options = [set(allnames) for i in xrange(16)]

tab = [bori, borr, addi, muli, addr, bani, gtri, setr, gtrr, seti, eqir, eqrr, mulr, eqri, gtir, banr]

for before, op, after in cases:
    n = 0
    ps = set()
    for opfun in ops:
        r = list(before)
        opfun(op[1], op[2], op[3], r)
        if r == after:
            n += 1
            ps.add(opfun.func_name)
    options[op[0]] &= ps
    if n >= 3:
        threecount += 1
    r = list(before)
    tab[op[0]](op[1], op[2], op[3], r)
    if r != after:
        raise Exception()
print threecount

for i in xrange(16):
    print i, options[i]

r = [0,0,0,0]
for op in program:
    tab[op[0]](op[1], op[2], op[3], r)
print r
