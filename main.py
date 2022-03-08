#!/usr/bin/env python3

from shlex import *
import re
import os
import sys
filename = "si.txt"
key = ''
whitespace = ' '
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
for op, p in enumerate(program):
    if key != whitespace:
        print(key)
        key = ''
    if nt == '':
        pass
        # nt = lex.next_token()
        # print(nt)
        # print(gt)
    else:
        if sp[0] == 'write':
            
            lex.push_token(gt)
            print(sp[0+1])
            # break
