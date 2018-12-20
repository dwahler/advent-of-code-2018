#!/usr/bin/env python

import sys, itertools, collections

ipreg = None
prog = []
for line in sys.stdin:
    line = line.strip()
    toks = line.split()
    if toks[0] == "#ip":
        ipreg = int(toks[1])
    else:
        prog.append(tuple([toks[0]]+map(int,toks[1:])))

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
oplookup = dict((op.func_name,op) for op in ops)

regs = [0]*6
regs[0] = 0
ip = 0
inscount = 0
while True:
    regs[ipreg] = ip
    if not (0 <= ip < len(prog)):
        break
    instr = prog[ip]
    if inscount % 1 == 0:
        print inscount, ip, instr, regs
    op = oplookup[instr[0]]
    op(*(list(instr[1:])+[regs]))
    ip = regs[ipreg]
    ip += 1
    inscount += 1

print regs

