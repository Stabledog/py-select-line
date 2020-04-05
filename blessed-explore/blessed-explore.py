#!/usr/bin/env python3.7

import sys
from blessed import Terminal

term = Terminal()

loc = term.get_location()
print(f"loc={loc}")
print(term.home + term.clear + term.move_y(term.height // 2))

print(term.black_on_darkkhaki(term.center('Press any key to continue.')))

# with term.cbreak(), term.hidden_cursor():
#     inp = term.inkey()

# print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))

#txt = [ l.strip() for l in open(sys.argv[1],'r').readlines() ]
txt = '''1 file-1
2 file-2
3 file-3
4 file-4'''

curColor=term.red

print("hello")
term.up(2)
print("world")

# Note: we can't know the cursor's current position, but we can move it relatively with term.up, term.down, term.move_x
# Since we know how many lines we're printing and the height of the terminal, we can get the job done.
y_offset = 0
loc = term.get_location()
with term.location() as curs:
    for line in txt.split('\n'):
        esc=term.move_xy(10, loc[0] + y_offset)
        sys.stdout.write( esc + term.green + f"[{y_offset}] {line} "  )
        y_offset += 1

#print(term.yellow("so this is yellow"))

inp = term.inkey()
