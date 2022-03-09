#!/usr/bin/env python3

from shlex import *
import re
import os
import sys
filename = "si.txt"

with open(filename, "r") as f:
    program = f.read()
tokens = [' ', 'var', 'write']
keywords = ['"', ';', '=']

lex = shlex(program)
gt = lex.get_token()
nt = lex.read_token()
sp = split(program)
# print(sp)
# print()
def write(op, sp, c, p, nt, program, gt):    
    if sp[0] == 'write':            
        lex.push_token(gt)
        # a = lex.pop_token()
        gt = lex.get_token()
        print(c)
        print(sp)
        
def sim(program):
    key = ''
    whitespace = ' '
    lex = shlex(program)
    gt = lex.get_token()
    nt = lex.read_token()
    sp = split(program)
    c = 0
    for p, op in enumerate(program):
        if op != whitespace:
            key += op
        if (p + 1 < len(program)):
            if program[p+1] == whitespace:
                return write(op, sp, c, p, nt, program, gt)
                # print(key)
                c += 1
                key = ''
        if nt == '':
            pass
            c += 1
            # nt = lex.next_token()
            # print(nt)
            # print(gt)
        else:
            if sp[0] == 'write':            
                lex.push_token(gt)
                # return write(op, sp, c, p, nt, program, gt)
                print(sp[c])
                c += 1
                # break
sim(program)
