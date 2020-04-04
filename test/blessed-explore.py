#!/usr/bin/env python3.7

from blessed import Terminal

term = Terminal()
print(term.home + term.clear + term.move_y(term.height // 2))

print(term.black_on_darkkhaki(term.center('Press any key to continue.')))

with term.cbreak(), term.hidden_cursor():
    inp = term.inkey()

print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))

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
with term.location() as curs:
    for line in txt.split('\n'):
        #print(term.red + term.on_green + "Red on green!" + term.normal)
        print(curColor(line))
        term.down(1)

print(term.yellow("so this is yellow"))
